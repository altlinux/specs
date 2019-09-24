Name:		nim-lang
Version:	1.0.0
Release:	alt1
License:	MIT
Summary:	A statically typed compiled systems programming language
Source:		https://nim-lang.org/download/nim-1.0.0.tar.xz
Patch:		nim-1.0.0-alt-install.patch
URL:		https://nim-lang.org
Group:		Development/Other

BuildRequires:	/proc

%description
Nim is a statically typed compiled systems programming language. It
combines successful concepts from mature languages like Python, Ada and
Modula.

%prep
%setup -n nim-%version
%patch -p0

%build
sh build.sh
bin/nim c koch
./koch tools
./koch docs

%install
mkdir -p %buildroot%_prefix
sh ./install.sh %buildroot/usr

%files
%doc %_datadir/nim/doc
%doc doc/html examples
%_bindir/*
%_localstatedir/nim/pkgs
%_prefix/lib/nim
%_sysconfdir/nim

%changelog
* Tue Sep 24 2019 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build for ALT

