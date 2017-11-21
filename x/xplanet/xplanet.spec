# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl gcc-c++
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	Render a planetary image into an X window
Name:		xplanet
Version:	1.3.1
Release:	alt1_5

License:	GPLv2+
Group:		Toys
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		https://gitweb.gentoo.org/repo/gentoo.git/plain/x11-misc/xplanet/files/xplanet-1.3.1-giflib.patch
URL:		http://%{name}.sourceforge.net

BuildRequires:	libexpat-devel
BuildRequires:	glib2-devel libgio libgio-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libgif-devel
BuildRequires:	libtiff-devel libtiffxx-devel
BuildRequires:	libnetpbm-devel
BuildRequires:	libpango-devel libpango-gir-devel
Requires:	fonts-ttf-gnu-freefont-mono
Source44: import.info

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window.  Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively.  The other terrestrial
planets may also be displayed. The Xplanet home page has links to
locations with map files.


%prep
%setup -q
%patch0 -p1 -b .gif

%if 0%{?fedora} >= 24
LANG=C grep -rl "inFile\.getline" . | \
	xargs sed -i.c++11 \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*!= NULL|static_cast<bool> (\1\2)|' \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*== NULL|(!(static_cast<bool> (\1\2)))|'
%endif

%build
%configure
%make_build -k

%install
CPPROG="cp -p" make DESTDIR=%{buildroot} install

ln -sf ../fonts/ttf/gnu-free/FreeMonoBold.ttf \
	%{buildroot}%{_datadir}/%{name}/FreeMonoBold.ttf

%files
%doc AUTHORS ChangeLog NEWS README TODO
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/xplanet

%changelog
* Mon Nov 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_5
- new version by request of oddity@

* Fri Mar 20 2015 Ilya Mashkin <oddity@altlinux.ru> 1.2.2-alt2
- fix build, thanks Eugeny Rostovtsev

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.2-alt1.qa1
- NMU: rebuilt for libtiff.so.5.

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2 (thx fedorawatch)
- patch1 merged upstream

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1.1.1
- rebuilt with perl 5.12

* Sat Aug 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.1-alt1.1
- rebuild with gcc4.3

* Fri Jul 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Nov 13 2008 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt3
- fix build with gcc4.3

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt2.1
- rebuild

* Tue Feb 14 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.0-alt2
- Enabled pnm support
- Removed xorg-x11-devel-static from buildrequires
- Added libXt-devel to buildrequires

* Fri Sep 09 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.0-alt1
- Initial build for Sisyphus
