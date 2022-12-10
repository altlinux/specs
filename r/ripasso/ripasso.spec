# spec file for package ripasso
#

# Not usable yet - 20210706
%def_without  gtk
# Not even buildable yet - 202010706
%def_without  qml

Name: ripasso
Version: 0.6.0
Release: alt1

Summary: a simple password manager written in Rust
Summary(ru_RU.UTF-8): простой парольный менеджер, написанный на Rust

License: %gpl3only
Group: Text tools
Url: https://github.com/cortex/ripasso

Packager: Nikolay A. Fetisov <naf@altlinux.org>


Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: vendor.tar
Source2: config.toml

Source10: ripasso.sh

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sat Dec 10 2022
# optimized out: ca-trust clang13.0 clang13.0-devel clang13.0-libs clang13.0-libs-support glibc-kernheaders-generic glibc-kernheaders-x86 libassuan-devel libgmp-devel libgpg-error libgpg-error-devel libsasl2-3 llvm-common llvm13.0-libs llvm15.0-libs pkg-config python-modules python2-base python3 python3-base rust sh4
BuildRequires: bzlib-devel clang libgpgme-devel libnettle-devel libssl-devel libxcb-devel

BuildRequires: rust-cargo
BuildRequires: /proc


%description
Ripasso is a simple password manager written in Rust.

The root crate ripasso is a library for accessing and
decrypting passwords stored in pass format (GPG-encrypted files),
with a file-watcher event emitter.

Multiple UI's in different stages of development are available
in subcrates.

%description -l ru_RU.UTF-8
Ripasso - простой менеджер паролей, написанный на Rust.



%prep
%setup
%patch0 -p1

# Rust packages, update them before new build!
tar xf %SOURCE1
install -Dm664 -- %SOURCE2 .cargo/config


%build
export CARGO_HOME=`pwd`/cargo
cargo build --release --offline

for d in cursive %{?_with_gtk:gkt} %{?_with_qml:qml}; do
   pushd $d
     cargo build --release --offline
   popd
done

%install
# Binary files:
mkdir -p -- %buildroot%_bindir
for d in cursive %{?_with_gtk:gkt} %{?_with_qml:qml}; do
   cp -a -- target/release/ripasso-$d %buildroot%_bindir/
done

# Wrapper script
install -m 0755 -- %SOURCE10  %buildroot%_bindir/ripasso

# Man pages:
mkdir -p -- %buildroot%_mandir/man1/

cp -a -- target/man-page/cursive/ripasso-cursive.1 %buildroot%_mandir/man1/

# Translations:
mkdir -p -- %buildroot%_datadir/%name
cp -a -- target/translations/*  %buildroot%_datadir/%name/

%files
%doc LICENCE README.md

%_bindir/%{name}*
%_man1dir/%{name}*
%_datadir/%name


%changelog
* Sat Dec 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.6.0-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.5.2-alt1
- New version

* Sun Jul 18 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.5.1-alt1.gita33ac767
- Fix build with Rust 1.53.0

* Fri Jul 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.5.1-alt1
- New version

* Wed Jul 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux Sisyphus
