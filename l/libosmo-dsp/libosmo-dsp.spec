# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install pkgconfig(fftw3f)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libosmo-dsp
%define major   0
%define libname lib%{name}%{major}
%define devname lib%{name}-devel
%define uname   Osmo-DSP

Name:             libosmo-dsp
Summary:          A library with SDR DSP primitives
Version:          0.3
Release:          alt1_2
License:          GPLv2+
Group:            Communications
URL:              http://cgit.osmocom.org/libosmo-dsp/
Source0:          http://cgit.osmocom.org/libosmo-dsp/snapshot/%{name}-%{version}.tar.bz2

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    pkgconfig(fftw3)
BuildRequires:    doxygen
BuildRequires:    graphviz
Source44: import.info

%description
A library with SDR DSP primitives.

%package -n %{libname}
Summary:          A library with SDR DSP primitives
Group:            Communications

%description -n %{libname}
Library files for libosmo-dsp.

%package -n %{devname}
Summary:          Development files for libosmo-dsp
Group:            Communications
Requires:         %{libname} = %{version}-%{release}
Provides:         %{name}-devel = %{version}-%{release}
Provides:         osmo-dsp-devel = %{version}-%{release}

%description -n %{devname}
Development files for libosmo-dsp.

%package doc
Summary:          Documentation for osmo-dsp
Group:            Documentation
BuildArch:        noarch

%description doc
HTML documentation for osmo-dsp.

%prep
%setup -q
autoreconf -fi

%build
%configure --disable-static

%make LDFLAGS="${LDFLAGS} -lm"

%install
%makeinstall_std

# remove libtool
rm -f %{buildroot}%{_libdir}/*.la

# fix docs location
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/libosmodsp %{buildroot}%{_docdir}/%{name}/html

cat > %{name}-doc.desktop << EOF
[Desktop Entry]
Version=1.0
Name=%{uname} Documentation
GenericName=%{uname} Documentation
Exec=xdg-open /usr/share/doc/%{name}/html/index.html
Icon=
Terminal=false
Type=Application
Categories=System;Documentation;X-Mageia-CrossDesktop;
EOF

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{name}-doc.desktop

%files -n %{libname}
%doc AUTHORS
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{devname}
%{_includedir}/osmocom
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files doc
%dir %{_docdir}/%{name}/html
%{_docdir}/%{name}/html/*
%{_datadir}/applications/%{name}-doc.desktop


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_2
- new version

