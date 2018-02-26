%define cid     \{73a6fe31-595d-460b-a920-fcc0f8843232\}
%define ciddir  %firefox_noarch_extensionsdir/%cid

Summary:	NoScript extension for Firefox
Name:		firefox-noscript
Version:	2.2.6
Release:	alt1
Source0:	noscript-%version.xpi
License:	GPL
Group:		Networking/WWW
URL:		http://noscript.net
Packager:	Alexey Gladkov <legion@altlinux.ru>
BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox
BuildRequires:  unzip

%description 
Extra protection for your Firefox: NoScript allows JavaScript,
Java (and other plugins) only for trusted domains of your
choice (e.g. your home-banking web site). This whitelist
based pre-emptive blocking approach  prevents exploitation
of security vulnerabilities (known and even unknown!) with
no loss of functionality.

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
	[ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 2.2.6-alt1
- New version (2.2.6).

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 2.1.2.5-alt1
- New version (2.1.2.5).

* Fri Apr 08 2011 Alexey Gladkov <legion@altlinux.ru> 2.1.0.1-alt1
- New version (2.1.0.1)

* Sun Jan 24 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.9.39-alt1
- New version (1.9.9.39)

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.3.3-alt1
- New version (1.9.3.3)

* Mon Jul 07 2008 Alexey Gladkov <legion@altlinux.ru> 1.7.6-alt1
- first build for ALT Linux.
