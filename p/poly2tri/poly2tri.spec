# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name poly2tri
%define version 1.0
%define date    20160413

%define major   1
%define minor   0
%define soname  %{major}.%{minor}
%define libname lib%{name}%{soname}
%define devname lib%{name}-devel

Name:           poly2tri
Version:        1.0
Release:        alt1_0.%{date}1
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD
Group:          Development/Other
URL:            https://github.com/jhasse/poly2tri
Source0:        %{name}-%{date}.tar.xz
# The Makefile was created for purposes of this package
# Upstream provides WAF, but it builds example apps and not the library
Source1:        %{name}-Makefile
BuildRequires:  libGL-devel
Source44: import.info

%description
Library based on the paper "Sweep-line algorithm for constrained Delaunay
triangulation" by V. Domiter and and B. Zalik.

%package -n     %{libname}
Summary:        A 2D constrained Delaunay triangulation library
Group:          System/Libraries
Obsoletes:      %{name} < 0.0-0.20130501hg26242d0aa7b8.2
Obsoletes:      %{name}-%{libname} < 0.0-0.20130501hg26242d0aa7b8.3

%description -n %{libname}
Library based on the paper "Sweep-line algorithm for constrained Delaunay
triangulation" by V. Domiter and and B. Zalik.

%package -n     %{devname}
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.0-0.20130501hg26242d0aa7b8.2
Obsoletes:      %{name}-%{devname} < 0.0-0.20130501hg26242d0aa7b8.3

%description -n %{devname}
Development files for %{name}.

%prep
%setup -q -n %{name}-%{date}
cp %{SOURCE1} %{name}/Makefile

iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && \
touch -r AUTHORS AUTHORS.conv && \
mv AUTHORS.conv AUTHORS

%build

%make -C %{name}

%install
install -Dpm0755 %{name}/lib%{name}.so.%{soname} %{buildroot}%{_libdir}/lib%{name}.so.%{soname}
ln -s lib%{name}.so.%{soname} %{buildroot}%{_libdir}/lib%{name}.so.%{major}
ln -s lib%{name}.so.%{soname} %{buildroot}%{_libdir}/lib%{name}.so

for H in %{name}/*/*.h %{name}/*.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

# Add a pkgconfig entry
cat > %{name}.pc << EOF
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: A 2D constrained Delaunay triangulation library
Version: 1.0-%{date}

Requires:
Libs: -L\${libdir} -l%{name}
Cflags: -I\${includedir}/%{name}
EOF
install -D -m644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%files -n       %{libname}
%doc AUTHORS LICENSE README.md
%{_libdir}/lib%{name}.so.%{major}*

%files -n       %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.201604131
- converted for ALT Linux by srpmconvert tools

