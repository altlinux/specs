Name: geshi
Version: 1.0.8.4
Release: alt1
BuildArch: noarch

Group: Networking/WWW
Summary: A many languages syntax highlighter for HTML
Summary(ru_RU.UTF-8): Подсветка синтаксиса множества языков для HTML
Url: http://qbnz.com/highlighter
License: GPL
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: php-engine >= 4.3.0

Source0: %name-%version.tgz

%description
GeSHi is a syntax highlighter for HTML, written in PHP. Basically, you input the
source you want to highlight and the name of the language you want to highlight
it in, and GeSHi returns the syntax-highlighted result. GeSHi supports many
different languages.


%description -l ru_RU.UTF-8
GeSHi подсвечивает синтаксис для HTML. Введите желаемый код и название языка, и
GeSHi вернет подсвеченный синтаксис. Поддерживает множество языков.

%prep
%setup -q

%build

%install

mkdir -p %buildroot%_datadir/%name
cp -r %name.php %name contrib %buildroot%_datadir/%name/ 

%files
%_datadir/%name
%doc docs/*

%changelog
* Sun Jul 19 2009 Michael A. Kangin <prividen@altlinux.org> 1.0.8.4-alt1
- Initial release

