Name: silver-searcher
Version: 1.0.2
Release: alt1

Summary: A code searching tool similar to ack, with a focus on speed.
License: GPL
Group: Development/Tools
Url: https://github.com/ggreer/the_silver_searcher/

Packager: %packager
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jun 07 2015
BuildRequires: clang liblzma-devel libpcre-devel zlib-devel

%description
Ag (silversearcher) is a code searching tool.
It is an order of magnitude faster than ack.
It ignores file patterns from .gitignore and .hgignore,
also it has it's own .agignore file.

%prep
%setup -q

%build
./build.sh

cd doc
bzip2 -9 ag.1
cd ..

%install
mkdir -p %buildroot%_bindir
install -pm755 ag %buildroot/%_bindir/

# Устанавливаем руководство.
mkdir -p %buildroot%_man1dir
install -pm644 doc/ag.1.* %buildroot/%_man1dir/

# Добавляем нехитрую документацию.
%define docdir %_docdir/%name-%version

mkdir -p %buildroot/%docdir
install -pm644 CONTRIBUTING.md %buildroot%docdir/
install -pm644 LICENSE %buildroot%docdir/
install -pm644 README.md %buildroot%docdir/

%files
%_bindir/ag
%_man1dir/ag.1.*
%dir %docdir
%docdir/*

%changelog
* Sat Dec 17 2016 Andrey Bergman <vkni@altlinux.org> 1.0.2-alt1
- Version update.

* Mon Oct 12 2015 Andrey Bergman <vkni@altlinux.org> 0.31.0-alt0.1
- Version update.

* Sat Jun 06 2015 Andrey Bergman <vkni@altlinux.org> 0.30.0-alt0.1
- Initial release for Sisyphus.

