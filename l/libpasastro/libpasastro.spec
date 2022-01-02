# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           libpasastro
Version:        1.4.1
Release:        alt1_1
Summary:        Pascal interface for standard astronomy libraries
Group:          Sciences/Astronomy
License:        GPLv2+
URL:            https://sourceforge.net/projects/libpasastro/
# Official stable version doesn't include yet fixes required upstream
# for packaging in Fedora, so we use svn version.
# Use the following commands to generate the tarball:
# svn export -r 9 svn://svn.code.sf.net/p/libpasastro/code/trunk libpasastro-1.0
# tar -cJvf libpasastro-1.0-svn.tar.xz libpasastro-1.0
Source0:        https://github.com/pchev/libpasastro/archive/v%{version}.tar.gz#/libpasastro-%{version}.tar.gz
#Source0:        https://downloads.sourceforge.net/%%{name}/%%{name}-%%{version}-src.tar.xz

# Patch to fix stripping and permissions of library files
# Since this is Fedora specific we don't ask upstream to include
Patch0:         libpasastro-1.0-fix-install.patch
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


# fix library path in install.sh script on 64bit
sed -i 's/\$destdir\/lib/\$destdir\/%{_lib}/g' ./install.sh

%build
mkdir -p plan404/obj
%make_build arch_flags="%{optflags}"


%install
%makeinstall_std PREFIX="%{buildroot}/usr"

%files
%doc %{_datadir}/doc/%{name}/
%{_libdir}/libpas*.so.*


%changelog
* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 1.4.1-alt1_1
- update by mgaimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- new version

