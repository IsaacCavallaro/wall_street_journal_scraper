CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS dollar_prices (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    price numeric(8,4) NOT NULL,
    date date NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    CONSTRAINT dollar_prices_date_price_key UNIQUE (date, price)
);

CREATE TABLE IF NOT EXISTS news_headlines (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    headline text NOT NULL,
    date date NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    CONSTRAINT news_headlines_date_headline_key UNIQUE (date, headline)
);

CREATE TABLE IF NOT EXISTS correlations (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    dollar_price_id uuid NOT NULL REFERENCES dollar_prices(id),
    news_headline_id uuid NOT NULL REFERENCES news_headlines(id),
    correlation numeric(8,4) NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    CONSTRAINT correlations_unique_key UNIQUE (dollar_price_id, news_headline_id)
);
