Name: manatee-open
Version: 2.151.5
Release: alt1

Summary: Manatee is a corpus management tool
License: LGPLv2+
Group: System/Libraries
Url: http://nlp.fi.muni.cz/trac/noske/wiki/Downloads
Packager: Kirill Maslinsky <kirill@altlinux.org>
BuildRequires: antlr3-tool finlib-devel gcc-c++ java-devel antlr3-C-devel libpcre-devel perl-devel python-module-distribute ruby libicu-devel libltdl7-devel
ExclusiveArch: x86_64


Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Manatee is a corpus management tool including corpus building and indexing,
fast querying and providing basic statistical measures. It utilitates a fast
indexing library called Finlib. 

%prep
%setup
%patch -p1

%build
#export MANATEE_REGISTRY=%_localstatedir/manatee
%configure --with-icu
%make_build

%install
%makeinstall_std

%files 
%_libdir/*.so.*
%_bindir/*
%python_sitelibdir/*.py*
%python_sitelibdir/_manatee.so
%doc doc/*

%changelog
* Wed Jan 31 2018 Kirill Maslinsky <kirill@altlinux.org> 2.151.5-alt1
- 2.151.5

* Wed Oct 26 2016 Kirill Maslinsky <kirill@altlinux.org> 2.139.3-alt3
- build only for x86_64 (i586 unsupported upstream)

* Wed Oct 19 2016 Kirill Maslinsky <kirill@altlinux.org> 2.139.3-alt2
- fix build

* Wed Oct 19 2016 Kirill Maslinsky <kirill@altlinux.org> 2.139.3-alt1
- 2.139.3

* Sat Dec 05 2015 Kirill Maslinsky <kirill@altlinux.org> 2.130.6-alt1
- 2.130.6

* Wed Mar 18 2015 Kirill Maslinsky <kirill@altlinux.org> 2.107.1-alt1
- 2.107.1

* Wed Oct 02 2013 Kirill Maslinsky <kirill@altlinux.org> 2.59.1-alt1
- 2.59.1

* Tue Apr 10 2012 Kirill Maslinsky <kirill@altlinux.org> 2.33.1-alt1
- Initial build for Sisyphus

