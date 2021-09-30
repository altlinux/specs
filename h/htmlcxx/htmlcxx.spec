# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name htmlcxx
%define		css_major 0
%define		css_minor 0
%define		major 3
%define		minor 1

%define		libname lib%{name}%{major}
%define		devel lib%{name}-devel
%define		cssdev libcssparser%{css_major}
%define		csslib libcssparser-devel

Name:		htmlcxx
Version:	0.87
Release:	alt3_2
Summary:	htmlcxx is a simple non-validating css1 and html parser for C++
Group:		Development/Other 
License:	LGPLv2
URL:		http://htmlcxx.sourceforge.net/
Source0:	https://sourceforge.net/projects/htmlcxx/files/v%{version}/%{name}-%{version}.tar.gz
Patch0:		htmlcxx-0.86-linking.patch
Source44: import.info

%description
htmlcxx is a simple non-validating css1 and html parser for C++.
Although there are several other html parsers available, htmlcxx has some
characteristics that make it unique: - STL like navigation of DOM tree,
using excelent's tree.hh library from Kasper Peeters.

- It is possible to reproduce exactly, character by character, the original
  document from the parse tree
- Bundled css parser
- Optional parsing of attributes
- C++ code that looks like C++ (not so true anymore)
- Offsets of tags/elements in the original document are stored in the nodes
  of the DOM tree

%package -n	%{devel}
Summary:	Development files
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{libname} < 0.8.6-4

%description -n	%{devel}
Development files

%package -n	%{libname}
Summary:	These are the main libraries
Group:		Development/Other 
Conflicts:	%{devel} < 0.8.6-4

%description -n	%{libname}
The main libraries

%package -n	%{cssdev}
Summary:	These are the css_parser development files
Group:		Development/Other 
Conflicts:	%{devel} < 0.8.6-4

%description -n	%{cssdev}
Development files for libcss_*

%package -n	%{csslib}
Summary:	These are the css_parser libraries
Group:		System/Libraries

%description -n	%{csslib}
Libraries containing the libcss_* files

%prep
%setup -q
%patch0 -p1


%build
%add_optflags -std=c++14
autoreconf -vfi
%configure
%make_build

%install
%makeinstall_std

# Delete static libraries
find %{buildroot} -name *.*a -delete

%files
%{_bindir}/%{name}

%files -n	%{libname}
%{_libdir}/libhtmlcxx.so.%{major}*

%files -n	%{devel}
%{_includedir}/%{name}/html/
%{_libdir}/libhtmlcxx.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n	%{cssdev}
%{_includedir}/%{name}/css/
%{_datadir}/%{name}/
%{_libdir}/libcss_parser.so
%{_libdir}/libcss_parser_pp.so

%files -n	%{csslib}
%{_libdir}/libcss_parser.so.%{css_major}
%{_libdir}/libcss_parser.so.%{css_major}.*
%{_libdir}/libcss_parser_pp.so.%{css_major}
%{_libdir}/libcss_parser_pp.so.%{css_major}.*


%changelog
* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 0.87-alt3_2
- fixed build with gcc11

* Mon Oct 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.87-alt2_2
- to Sisyphus (closes: #39037)

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1_2
- update by mgaimport

* Sat Jan 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1_1
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1_5
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1_4
- new version

