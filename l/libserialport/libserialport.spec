Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libudev)
# END SourceDeps(oneline)
Name:           libserialport
Version:        0.1.0
Release:        alt1_2
Summary:        Library for accessing serial ports
License:        LGPLv3+
URL:            http://sigrok.org/wiki/%{name}
Source0:        http://sigrok.org/download/source/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  libudev-devel
BuildRequires:  doxygen graphviz

Provides: bundled(jquery) = 1.7.1
Source44: import.info

%description
libserialport is a minimal library written in C that is intended to take care
of the OS-specific details when writing software that uses serial ports.

By writing your serial code to use libserialport, you enable it to work
transparently on any platform supported by the library.

The operations that are supported are:

- Port enumeration (obtaining a list of serial ports on the system).
- Opening and closing ports.
- Setting port parameters (baud rate, parity, etc).
- Reading, writing and flushing data.
- Obtaining error information.


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Group:          Documentation
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation for developing software
with %{name}.


%prep
%setup -q

%build
%configure --disable-static
V=1 make %{?_smp_mflags}

# This builds documentation for the -doc package
make %{?_smp_mflags} doc


%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc COPYING README
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc doxy/html-api/


%changelog
* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_2
- new version

