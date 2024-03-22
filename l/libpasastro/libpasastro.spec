# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           libpasastro
Version:        1.4.2
Release:        alt1_1
Summary:        Pascal interface for standard astronomy libraries
Group:          Sciences/Astronomy
License:        GPL-2.0-or-later AND LGPL-2.1-only AND BSD-3-Clause
URL:            https://sourceforge.net/projects/libpasastro/
Source0:        https://github.com/pchev/libpasastro/archive/v%{version}/libpasastro-%{version}.tar.gz
#Source0:        https://downloads.sourceforge.net/%%{name}/%%{name}-%%{version}-src.tar.xz

# Patch to fix stripping and permissions of library files
# Since this is Fedora specific we don't ask upstream to include
Patch0:         libpasastro-1.0-fix-install.patch

Provides:       libpasgetdss = %{version}
Provides:       libpasplan404 = %{version}
Provides:       libpaswcs = %{version}
Source44: import.info

%description
Libpasastro provides shared libraries to interface Pascal program 
with standard astronomy libraries.
libpasgetdss.so : Interface with GetDSS to work with DSS images.
libpasplan404.so : Interface with Plan404 to compute planets position.
libpaswcs.so : Interface with libwcs to work with FITS WCS.

%prep
%setup -q
%patch0 -p1


# do not install docs, use %%doc macro
sed -i '/\$destdir\/share/d' ./install.sh

# fix library path in install.sh script on 64bit
sed -i 's/\$destdir\/lib/\$destdir\/%{_lib}/g' ./install.sh

%build
mkdir -p plan404/obj
%make_build arch_flags="%{optflags}"

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}

%files
%doc changelog copyright README.md
%{_libdir}/libpas*.so.1
%{_libdir}/libpas*.so.1.*


%changelog
* Fri Mar 22 2024 Igor Vlasenko <viy@altlinux.org> 1.4.2-alt1_1
- update by mgaimport

* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 1.4.1-alt1_1
- update by mgaimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- new version

