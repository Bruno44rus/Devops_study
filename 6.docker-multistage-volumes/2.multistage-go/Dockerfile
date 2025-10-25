FROM golang:1.22 AS builder
WORKDIR /app
COPY . .
RUN go build -o app main.go

FROM debian:bookworm-slim
COPY --from=builder /app/app .
RUN chmod +x app
CMD ["app"]
