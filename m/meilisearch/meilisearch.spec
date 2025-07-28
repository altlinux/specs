%define _unpackaged_files_terminate_build 1

Name:    meilisearch
Version: 1.14.0
Release: alt1

Summary: Meilisearch HTTP server
License: MIT
Group:   Other
URL:     https://www.meilisearch.com
VCS:     https://github.com/meilisearch/meilisearch.git

Source0: %name-%version.tar
Source1: mecab-ko-dic-2.1.1-20180720.tar.gz
Source2: unidic-mecab-2.1.2.tar.gz
Source3: lindera-ko-dic.tar
Source4: lindera-unidic.tar
Source5: build.zip
Source6: smol-songs.csv.gz
Source7: smol-songs-1_2.csv.gz
Source8: smol-songs-3_4.csv.gz
Source9: smol-songs-4_4.csv.gz
Source10: smol-wiki-articles.csv.gz
Source11: smol-wiki-articles-1_2.csv.gz
Source12: smol-wiki-articles-3_4.csv.gz
Source13: smol-wiki-articles-4_4.csv.gz
Source14: movies.json.gz
Source15: movies-1_2.json.gz
Source16: movies-3_4.json.gz
Source17: movies-4_4.json.gz
Source18: nested_movies.json.gz
Source19: smol-all-countries.jsonl.gz
Source20: %name.service

BuildRequires: /proc
BuildRequires: rust-cargo

%description
A lightning-fast search engine API bringing AI-powered hybrid search
to your sites and applications.
Meilisearch helps you shape a delightful search experience in a snap,
offering features that work out of the box to speed up your workflow.

%prep
%setup
# 1. Download files using links in vendor/lindera-ko-dic/build.rs and vendor/lindera-unidic/build.rs:
# - https://Lindera.dev/mecab-ko-dic-2.1.1-20180720.tar.gz
# - https://Lindera.dev/unidic-mecab-2.1.2.tar.gz
# Put downloaded archives to .gear.
# 2. Build lindera dictionaries on your computer:
# $ git clone https://github.com/lindera/lindera.git
# $ cd lindera
# $ cargo build --features=ko-dic
# $ find target/ -name "char_def.bin" | grep lindera-ko-dic
# Example output: target/debug/build/lindera-ko-dic-<hash>/out/lindera-ko-dic/char_def.bin
# Tar folder target/debug/build/lindera-ko-dic-<hash>/out/lindera-ko-dic and put to your meilisearch/.gear
# Do the same with lindera-unidic (cargo build --features=unidic)
# 3. Download package mini-dashboard from the url in crates/Cargo.toml:assets-url and put it into .gear.
# 4. Download datasets from url in crates/benchmarks/build.rs if it is necessary (check datasets list in this file).

cp %{SOURCE1} vendor/lindera-ko-dic/
cp %{SOURCE2} vendor/lindera-unidic/
cp %{SOURCE5} crates/meilisearch/
mkdir -p datasets
gunzip -c %{SOURCE6} > datasets/smol-songs.csv
gunzip -c %{SOURCE7} > datasets/smol-songs-1_2.csv
gunzip -c %{SOURCE8} > datasets/smol-songs-3_4.csv
gunzip -c %{SOURCE9} > datasets/smol-songs-4_4.csv
gunzip -c %{SOURCE10} > datasets/smol-wiki-articles.csv
gunzip -c %{SOURCE11} > datasets/smol-wiki-articles-1_2.csv
gunzip -c %{SOURCE12} > datasets/smol-wiki-articles-3_4.csv
gunzip -c %{SOURCE13} > datasets/smol-wiki-articles-4_4.csv
gunzip -c %{SOURCE14} > datasets/movies.json
gunzip -c %{SOURCE15} > datasets/movies-1_2.json
gunzip -c %{SOURCE16} > datasets/movies-3_4.json
gunzip -c %{SOURCE17} > datasets/movies-4_4.json
gunzip -c %{SOURCE18} > datasets/nested_movies.json
gunzip -c %{SOURCE19} > datasets/smol-all-countries.jsonl

%build
# Lindera settings
LINDERA_VERSION="0.43.1"
CACHE_DIR=$(pwd)/.lindera-cache

mkdir -p "$CACHE_DIR/$LINDERA_VERSION"
tar -xf %{SOURCE3} -C "$CACHE_DIR/$LINDERA_VERSION/"
tar -xf %{SOURCE4} -C "$CACHE_DIR/$LINDERA_VERSION/"

# ENV vars for vendor/lindera-dictionary/src/assets.rs
export LINDERA_CACHE="$CACHE_DIR"
export CARGO_PKG_VERSION="$LINDERA_VERSION"

# ENV var for crates/benchmarks/build.rs 
export MILLI_BENCH_DATASETS_PATH=%_builddir/%name-%version/datasets

cargo build %_smp_mflags --offline --release --locked

%install
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name
install -Dp target/release/%name -t %buildroot%_bindir
install -Dp target/release/meilitool -t %buildroot%_bindir
install -Dm 0644 config.toml -t %buildroot%_sysconfdir/%name
install -Dm 0644 %{SOURCE20} %buildroot%_unitdir/%name.service

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -g %name -c 'Meilisearch daemon' \
        -s /dev/null  -d %_localstatedir/%name %name 2>/dev/null ||:

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc *.md
%_bindir/%name
%_bindir/meilitool
%dir %attr(0770,root,%name) %_logdir/%name
%dir %attr(0750,root,%name)%_sysconfdir/%name
%dir %attr(0750,%name,%name)%_localstatedir/%name
%_unitdir/%name.service
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/config.toml

%changelog
* Fri Jun 20 2025 Aleksandr Gamzin <gamzin@altlinux.org> 1.14.0-alt1
- 1.14.0
- Initial build

