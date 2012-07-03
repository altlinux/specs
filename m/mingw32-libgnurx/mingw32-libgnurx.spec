BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-libgnurx
Version:        2.5.1
Release:        alt1_7
Summary:        MinGW Regex library

License:        LGPLv2+
Group:          System/Libraries
URL:            http://mingw.sourceforge.net/
Source0:        http://kent.dl.sourceforge.net/sourceforge/mingw/mingw-libgnurx-%{version}-src.tar.gz
Source1:        mingw32-libgnurx-configure.ac
Source2:        mingw32-libgnurx-Makefile.am
Patch0:         mingw32-libgnurx-honor-destdir.patch

BuildArch:      noarch

BuildRequires:  autoconf automake libtool
BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
Source44: import.info

%description
MinGW Windows regular expression library.


%package static
Summary:        Static version of the MinGW Windows regular expression library
Requires:       %{name} = %{version}-%{release}
Group:          System/Libraries

%description static
Static version of the MinGW Windows regular expression library.




%prep
%setup -q -n mingw-libgnurx-%{version}
%patch0 -p0

# The Makefile which is delivered with this package can't create static
# libraries and misnames the resulting import libraries
# So replace the buildsystem by a more proper one
cp %{SOURCE1} configure.ac
cp %{SOURCE2} Makefile.am
touch NEWS
touch AUTHORS
libtoolize --copy
aclocal
autoconf
automake --add-missing

%build
%{_mingw32_configure} --enable-static --enable-shared
make %{?_smp_mflags}


%install

# make install expects %{_mingw32_includedir} to exist
mkdir -p $RPM_BUILD_ROOT%{_mingw32_includedir}

make DESTDIR=$RPM_BUILD_ROOT install

# make install installs two import libraries named libgnurx.a and
# libgnurx.dll.a. As most applications requiring regex functions
# try to perform 'gcc -lregex' we rename the import libraries for this to work
mv $RPM_BUILD_ROOT%{_mingw32_libdir}/libgnurx.a $RPM_BUILD_ROOT%{_mingw32_libdir}/libregex.a
mv $RPM_BUILD_ROOT%{_mingw32_libdir}/libgnurx.dll.a $RPM_BUILD_ROOT%{_mingw32_libdir}/libregex.dll.a
mv $RPM_BUILD_ROOT%{_mingw32_libdir}/libgnurx.la $RPM_BUILD_ROOT%{_mingw32_libdir}/libregex.la
sed -i s/gnurx/regex/ $RPM_BUILD_ROOT%{_mingw32_libdir}/libregex.la

# Drop the man pages
rm -rf $RPM_BUILD_ROOT%{_mingw32_datadir}/man


%files 
%doc COPYING.LIB
%{_mingw32_bindir}/libgnurx-0.dll
%{_mingw32_includedir}/regex.h
%{_mingw32_libdir}/libregex.dll.a
%{_mingw32_libdir}/libregex.la

%files static
%{_mingw32_libdir}/libregex.a


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_7
- initial release by fcimport

