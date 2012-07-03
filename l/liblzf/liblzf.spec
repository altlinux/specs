%add_optflags %optflags_shared
Name:           liblzf
Version:        3.6
Release:        alt2_3
Summary:        Small data compression library

Group:          System/Libraries
License:        BSD or GPLv2+
URL:            http://oldhome.schmorp.de/marc/liblzf.html
Source0:        http://dist.schmorp.de/liblzf/liblzf-%{version}.tar.gz
# Adds autoconf and in particular support for building shared libraries.
# 7th Feb 2011 - Mail sent upstream to author. Awaiting conclusion. 
Patch0:         liblzf-%{version}-autoconf.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Source44: import.info

%description
LibLZF is a very small data compression library. It consists 
of only two .c and two .h files and is very easy to 
incorporate into your own programs.  The compression algorithm 
is very, very fast, yet still written in portable C.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       liblzf = %{version}-%{release}

%if 0%{?el4}%{?el5}
%endif


%description    devel
The liblzf-devel package contains libraries and header files for
developing applications that use liblzf.

%prep
%setup -q
%patch0 -p1

%build
sh ./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# Binary does different things depending
# on the name it is called by.
pushd %{buildroot}%{_bindir}
ln -s lzf unlzf
#Leave lzcat  out since it conflicts with xz-lzma-compat.
#If ever needed would need an alternative setting up,
#if someone ever asks I'll do it.
#ln -s lzf lzcat
popd
rm -f %{buildroot}%{_libdir}/liblzf.la

%files
%{_bindir}/lzf
%{_bindir}/unlzf
%{_libdir}/liblzf.so.*
# The cs directory contains a .net implementation of lzf.
# Will happily add a .net sub package if given a patch.
%doc README Changes LICENSE cs

%files devel
%{_includedir}/lzf.h
%{_libdir}/liblzf.so
%{_libdir}/pkgconfig/liblzf.pc

%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.6-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.6-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_2
- initial import by fcimport

