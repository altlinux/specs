Name:           nfstrace
License:        GPLv2+
Group:          Monitoring
Summary:        `nfstrace` is an NFS tracing/monitoring/capturing/analyzing tool.

Version:        0.3.1
Release:        alt1

Packager:	Denis Pynkin <dans@altlinux.org>

Source:         %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: clang-devel
BuildRequires: gcc-c++
BuildRequires: libpcap-devel

%description
`nfstrace` performs live Ethernet 1 Gbps - 10 Gbps packets capturing and helps to
determine NFS procedures in raw network traffic. Furthermore, it performs
filtration, dumping, compression, statistical analysis, visualization and
provides the API for custom pluggable analysis modules.

%package	plugins
Summary:	Shared library files for %{name}
Group:		Monitoring
Requires:	%{name}
%description	plugins
The %{name}-plugins package contains additional plugins for %{name}.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C++
%description	devel
The %{name}-devel package contains development part of %{name}.


%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

#check
#cmake_build test

%files
%defattr(-,root,root)
%doc README.md LICENSE docs/nfstrace_manual.pdf
%{_bindir}/%name
%{_man8dir}/*

%files plugins
%defattr(-,root,root)
%{_libexecdir}/%name/*.so

%files devel
%doc docs/graphics.pdf
%defattr(-,root,root)
%dir %{_includedir}/%name
%dir %{_includedir}/%name/api
%{_includedir}/%name/api/*.h

%changelog
* Tue Dec 16 2014 Denis Pynkin <dans@altlinux.org> 0.3.1-alt1
- New version

* Sun Nov 16 2014 Denis Pynkin <dans@altlinux.org> 0.3.0-alt1
- Initial version


