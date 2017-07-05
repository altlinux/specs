Name:           nfstrace
License:        GPLv2+
Group:          Monitoring
Summary:        `nfstrace` is an NFS tracing/monitoring/capturing/analyzing tool.

Version:        0.4.0
Release:        alt2.2

Packager:	Denis Pynkin <dans@altlinux.org>

Source:         %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: clang-devel
BuildRequires: gcc-c++
BuildRequires: libpcap-devel
#BuildRequires: libgmock-devel
BuildRequires: libjson-c-devel
BuildRequires: libncurses-devel
BuildRequires: ctest
BuildRequires: python


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
BuildArch:	noarch
%description	devel
The %{name}-devel package contains development part of %{name}.


%prep
%setup -q

%build
%add_optflags -Wno-error=misleading-indentation
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
%cmake_build test

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
* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt2.2
- Updated build dependencies

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt2.1
- Rebuild with new version of libjson

* Thu Apr 16 2015 Denis Pynkin <dans@altlinux.org> 0.4.0-alt2
- Fixed architecture for devel package.

* Thu Mar 12 2015 Denis Pynkin <dans@altlinux.org> 0.4.0-alt1
- New version
- Test enabled

* Tue Dec 16 2014 Denis Pynkin <dans@altlinux.org> 0.3.1-alt1
- New version

* Sun Nov 16 2014 Denis Pynkin <dans@altlinux.org> 0.3.0-alt1
- Initial version


