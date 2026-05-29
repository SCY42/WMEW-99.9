[![kr](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-003e89)](https://github.com/PseudoCardiac/WMEW-99.9/blob/main/README.md) [![en](https://img.shields.io/badge/English-cfa64d)](https://github.com/PseudoCardiac/WMEW-99.9/blob/main/README.en.md) [![jp](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-bc002d)](https://github.com/PseudoCardiac/WMEW-99.9/blob/main/README.jp.md)

# 概要

このプログラムは、ビデオゲーム『Mewgenics』に登場する架空のラジオ局「WMEW 99.9」（を再構成したようなもの）をシステムコンソール上で再生します。音楽だけでなく、ニュース、コールレター、楽曲コメント、さらには広告まで楽しむことができます。

# インストール方法

著作権保護のため、再生する音声ファイルは各自で用意してください。

## 音声ファイル

> `Steam\steamapps\common\Mewgenics` にある `resource.gpak` ファイルからアセットを抽出してください。

* SteamでMewgenicsを右クリック → 「管理」→ 「ローカルファイルを閲覧」を選択すると、フォルダーをすぐに開けます。

* 抽出方法は問いませんが、作者は [GPAK-Extractor](https://github.com/ShootMe/GPAK-Extractor) を使用しました。以下の説明も、このツールの出力構成を前提としています。

* 必要なのは、抽出された `audio\music\radio` フォルダーのみです。つまり、`audio` フォルダー内の `music` フォルダー、その中にある `radio` フォルダーです。

## WMEW 99.9.exe

1. [Releasesページ](https://github.com/SCY42/WMEW-99.9/releases) の Assets 欄から `WMEW_99.9.zip` をダウンロードしてください。

2. ZIPファイルを展開した後、前の手順で取得した `radio` フォルダーを `WMEW_99.9` フォルダー内へ移動してください。

その後、`WMEW_99.9` フォルダー自体は好きな場所へ移動して構いませんが、中のファイル名を変更したり、別の場所へ移動したりしないでください。

# Tips

## 音量調整

このプログラムには独自の音量調整機能はありません。システムのボリュームミキサーから、アプリごとの音量調整機能を利用してください。Windowsでは、音量アイコンを右クリックすると「音量ミキサーを開く」が表示されます。

## 一部楽曲ファイル名の不一致について

5曲については、対応するイントロ／アウトロ用ファイルと名前が一致していないため、イントロ／アウトロが正常に再生されません。些細な問題ではありますが、すべてのイントロ／アウトロを正しく楽しみたい場合は、`radio\songs` フォルダー内の以下のファイル名を変更してください。

1. `crystaline_dreams` → `crystalline_dreams`

2. `final_boss` → `dig_your_own_grave`

3. `fleas_and_parasites_v1` → `fleas_parasites`

4. `the_crack_of_doom` → `crack_of_doom`

5. `you_know_who` → `guillotina`

## お問い合わせ

使用中に問題が発生した場合や、不具合を発見した場合は、お気軽にご連絡ください。

[![gmail](https://img.shields.io/badge/Gmail-white?logo=gmail)](mailto:pseudocardiac@gmail.com) [![x](https://img.shields.io/badge/X_(Twitter)-black?logo=x)](https://x.com/PseudoCardiac) [![discord](https://img.shields.io/badge/Discord-white?logo=discord)](https://discord.gg/hW2AFmtdaw)