# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           mhgui
Version:        0.2
Release:        alt2.1
Summary:        A simple GUI library for MakeHuman

Group:          System/Libraries
License:        GPLv3+
URL:            http://www.dedalo-3d.com
Source0:        http://downloads.sourceforge.net/makehuman/mhgui-%{version}.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>

Patch0:         mhgui-0.1-pkgconfig.patch
Patch1:         mhgui-0.2-newpng.patch

BuildRequires:  animorph-devel >= 0.3
BuildRequires:  libfreeglut-devel
BuildRequires:  libpng-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel
Source44: import.info
      

%description
A simple GUI library for MakeHuman


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
# We need to fix CRLF first
for f in mhgui*.in config.h.in ; do
  sed -i 's/\r//' $f
  touch -r README $f
done
%patch0 -p1 -b .pkgconfig
%patch1 -p1 -b .png15


%build
%configure --disable-static --with-x

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p -c"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Removes doc
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc


%files
%doc AUTHORS COPYING TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2-alt2.1
- Rebuild with new dependencies

* Wed Mar 19 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2-alt2
- Build for Sisyphus

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_16
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_15
- initial fc import

