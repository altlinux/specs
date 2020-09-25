# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/swig gcc-c++ python-devel swig
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libhocr
%define version 0.10.18
# Override default upstream location [/usr/share/doc/libhocr]
%global	hocrdocdir	%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

%define major	0
%define libname	libhocr%{major}
%define devname	libhocr-devel

Name:		libhocr
Version:	0.10.18
Release:	alt1_10
Summary:	A Hebrew optical character recognition library

Group:		System/Libraries
License:	GPLv3+
URL:		http://hocr.berlios.de
Source0:	http://download.berlios.de/hocr/%{name}-%{version}.tar.bz2
Patch1:		libhocr-fix-automake.patch
Patch2:		libhocr-0.10.18-linking.patch
BuildRequires:	libfftw3-devel
BuildRequires:	libhspell-devel
BuildRequires:	libtiff-devel libtiffxx-devel
BuildRequires:	gtk2-devel
BuildRequires:	glib2-devel libgio-devel
Obsoletes:	%{name}-gtk < 0.10.18-9
Obsoletes:	%{name}-python < 0.10.18-9
Source44: import.info

%description
LibHocr is a GNU Hebrew optical character recognition library. It scans
document images, improve the image, analyzes the page layout, recognizes
the characters and outputs the text. The output texts are now editable
text, ready for your blog, word processor or any other use.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	libhocr = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{libname}
Summary:	A Hebrew optical character recognition library
Group:		System/Libraries
Conflicts:	%{name} < 0.10.18-2
Conflicts: libhocr < 0.10.18
Obsoletes: libhocr < 0.10.18

%description -n %{libname}
LibHocr is a GNU Hebrew optical character recognition library. It scans
document images, improve the image, analyzes the page layout, recognizes
the characters and outputs the text. The output texts are now editable
text, ready for your blog, word processor or any other use.

%prep
%setup -q
%patch1 -p1
%patch2 -p1


%build
autoreconf -vfi
export CFLAGS="%optflags -Werror-implicit-function-declaration"
%configure \
	--disable-static \
	--disable-hocr-gtk \
	--disable-python
make

%install
%makeinstall_std \
	hocrdocdir=%{hocrdocdir}	\
	examples_binding_dir=%{hocrdocdir}/examples/bindings

# we don't want these
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}/%{hocrdocdir}/NEWS		# Empty, not usefull.
rm -f %{buildroot}/%{hocrdocdir}/INSTALL	# Not needed anymore ;-)

# "fix" icons
%if 0
for i in 48 128; do
	install -Dpm644 ./examples/hocr-gtk/hocr1-${i}.png \
		%{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/hocr.png
done
rm -rf %{buildroot}%{_datadir}/pixmaps/
%endif

%files
%doc %dir %{hocrdocdir}
%doc %{hocrdocdir}/AUTHORS
%doc %{hocrdocdir}/COPYING
%doc %{hocrdocdir}/ChangeLog
%doc %{hocrdocdir}/HACKING
%doc %{hocrdocdir}/README
%{_bindir}/hocr
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/%{name}*.so.%{major}
%{_libdir}/%{name}*.so.%{major}.*

%files -n %{devname}
%doc %{hocrdocdir}/examples
%doc %{_mandir}/man3/*.3*
%{_includedir}/%{name}/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc


%changelog
* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.18-alt1_10
- new version

* Sun Jan 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt4_30
- fixed build

* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt3_30
- fixed self-br thanks to rider@

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_30
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_28
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_24
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_23
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_22
- update to new release by fcimport

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_21
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_17
- update to new release by fcimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_16
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_15
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_14
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_12
- update to new release by fcimport

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.17-alt2_11.1
- Rebuilt with libtiff5

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_11
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_10
- update to new release by fcimport

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_9
- spec cleanup

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt1_9
- initial import by fcimport

