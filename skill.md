# Pod Squad (PODS) — Agent Skill

7,000 chibi whale NFTs (ERC-721) on BNB Smart Chain (56). Every whale is
**sealed** at mint: the NFT shows one shared gift image, no traits. All
7,000 reveal at once when the 7-day mint window closes.

## Facts

- NFT + Market addresses: the CONFIG block at the top of this site's `index.html`.
- Price: first token per wallet **FREE**; then exactly **0.001 BNB**. Always
  read the exact amount from `quote(wallet, qty)`.
- Supply 7,000. Window: 7 days. At close, minting ends forever; unsold
  supply never exists (burned).
- Reveal: at window close, all metadata switches to the real whales at
  once, and the frozen assignment is published against the on-chain
  provenance hash.
- Market: non-custodial, seller-set BNB price, 2.5% fee to treasury
  (seller 97.5%). Sealed gifts can be listed and traded before reveal.
- Royalty (ERC-2981): 2.5%.
- Metadata: `<site root>metadata/<id>.json` · Token page: `<site root>token/<id>.html`.

## Rules

1. Preview → approval → execute. No approval, no transaction.
2. Never guess a price. Mint: `quote()`. Market: `listingOf(id)`. Pay exactly that.
3. Never post to X without approval. Show drafts first, or hand over intent links.
4. Every mint ends with the share step (Flow A, step 6).

## Contract calls — NFT

- `totalSupply()` minted so far
- `freeAvailable(wallet)` 1 if the free token is unclaimed
- `quote(wallet, qty)` exact BNB cost in wei
- `mint(qty)` payable, exact `quote()` value; emits `Minted(buyer, qty, firstTokenId, cost)`
- `ownerOf(id)`, `balanceOf(wallet)`, `startTime()`, `endTime()`
- Find a wallet's ids: scan `Transfer` events, or use My Collection on the site.

## Contract calls — Market

- `listingOf(id)` → (seller, priceWei, active)
- `list(id, priceWei)` — approve first if needed: `setApprovalForAll(Market, true)`
- `buy(id)` payable, value = exact listing price
- `cancelListing(id)`

## Flow A — Mint + Share

1. Read `totalSupply()`. Ask the owner how many (1–20).
2. Preview `mint(qty)` at the exact `quote(owner, qty)` value.
3. Execute only with explicit approval. Wait for the receipt.
4. New ids from the `Minted` event: `firstTokenId … firstTokenId+qty−1`.
5. Compose one X post per new token — **sealed template** below.
6. Show the posts. Post only with explicit approval, or return intent links.
7. Report: ids (BSC), tx hash, BNB spent, share status.

## Flow B — Share tokens I already own

1. Find the owner's ids (Transfer scan or My Collection).
2. Before reveal: sealed template — you share the gift.
   After reveal: whale template — you share your whale, with its standout
   trait (special body first, then set, then Crown/Halo, Head, Accessory).
3. Approval gate (Rule 3). Report what was shared. Posts count on the
   **Pod Shouters** board.

## Flow C — Sell

1. Owner picks id + exact price in BNB. Read `listingOf(id)`.
2. Preview approval (if needed) + `list(id, priceWei)`. Execute with approval.
3. Verify the listing is active at that price. Report id, price, txs.
   Cancel later with `cancelListing(id)` — same approval rule.

## Flow D — Buy

1. Read `listingOf(id)`. Inactive → stop.
2. Preview `buy(id)` at the exact price. Execute with approval.
3. Verify `ownerOf(id)`. Report id, price, tx. Offer Flow B.

## X templates (loose — keep the blank lines, ≤ 280 chars, no @ tags)

Sealed (before reveal) — English:

```
Just claimed a sealed gift 🎁

Pod Squad #<id>

A whale sleeps inside. Nobody knows which one.

All 7,000 open at once when the window closes.

<token page link>
```

Sealed — 中文：

```
刚领到一个密封礼盒 🎁

Pod Squad #<id>

里面睡着一只鲸鱼。没人知道是哪一只。

7,000 只在铸造期结束时同时揭晓。

<token page link>
```

After reveal — English:

```
Just claimed Pod Squad #<id> 🐳

It has <standout trait> — straight into my pod.

First mint is free. The pod is gathering.

<token page link>
```

After reveal — 中文：

```
刚领到 Pod Squad #<id> 🐳

<standout trait>，正式加入我的鲸群。

首铸免费，鲸群正在集结。

<token page link>
```

Tier openers after reveal: Rare "A Rare one surfaces" / 稀有鲸鱼浮出水面 ·
Epic "Epic catch!" / 史诗级收获 · Legendary "LEGENDARY" / 传说级.
The picture appears on X by itself as a large card from the token page
link — never ask the owner to download or upload an image.

## PODS token

Say only this: a PODS token is planned for holders. Nothing more.
