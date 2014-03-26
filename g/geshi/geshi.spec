Name: geshi
Version: 1.0.8.11
Release: alt1

Summary: A many languages syntax highlighter for HTML
Summary(ru_RU.UTF-8): Подсветка синтаксиса множества языков для HTML

Group: Networking/WWW
License: GPL
Url: http://qbnz.com/highlighter

Packager: Michael A. Kangin <prividen@altlinux.org>

BuildArch: noarch

Requires: php-engine >= 4.3.0

# Source-url: http://prdownloads.sf.net/geshi/geshi/GeSHi%%20%version/GeSHi-%version.tar.gz
Source: %name-%version.tar

%description
GeSHi is a syntax highlighter for HTML, written in PHP. Basically, you input the
source you want to highlight and the name of the language you want to highlight
it in, and GeSHi returns the syntax-highlighted result. GeSHi supports many
different languages.


%description -l ru_RU.UTF-8
GeSHi подсвечивает синтаксис для HTML. Введите желаемый код и название языка, и
GeSHi вернет подсвеченный синтаксис. Поддерживает множество языков.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/%name/
cp -r %name.php %name contrib %buildroot%_datadir/%name/

%files
%_datadir/%name/
%doc docs/*

%changelog
* Wed Mar 26 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0.8.11-alt1
- new version 1.0.8.11 (with rpmrb script)
- cleanup spec

* Sun Jul 19 2009 Michael A. Kangin <prividen@altlinux.org> 1.0.8.4-alt1
- Initial release

