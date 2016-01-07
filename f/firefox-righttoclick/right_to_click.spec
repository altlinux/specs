# SPEC file for the RightToClick Firefox extension

%define rname	righttoclick
%define cid	\{cd617375-6743-4ee8-bac4-fbf10f35729e\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	2.9.6
Release:	alt1

Summary:	RightToClick Firefox extension
Summary(ru_RU.UTF-8):	расширение RightToClick для Firefox

License:	%mpl 1.1
Group:		Networking/WWW
URL:		https://addons.mozilla.org/ru/firefox/addon/righttoclick/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
RightToClick Firefox extension enables right-click, text selection,
context-menu, drag&drop and much more where it is disabled by
Javascript.

%description -l ru_RU.UTF-8
Расширение RightToClick для Firefox позволяет включить обработку
нажатий правой кнопки мыши, выделение и копирование текста,
контекстное меню и многое другое, что было отключено на
странице средствами JavaScript.

%prep
%setup -c

# RPM call unzip with -Lq keys, effectivly kills all mixed-case filenames in archive
rm -rf -- ./*
unzip -q %SOURCE0
subst 's/23\./24./' install.rdf

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.9.6-alt1
- New version
- Signed version to work with Firefox >= 43.x

* Sun Nov 03 2013 Andrey Cherepanov <cas@altlinux.org> 2.9.5-alt1.1
- Adapt for Firefox 24.x

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.9.5-alt1
- New version

* Tue Jun 11 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.9.4-alt1
- Initial build for ALT Linux Sisyphus
