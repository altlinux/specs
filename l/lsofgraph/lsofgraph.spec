
Name: lsofgraph
Version: 1.0.0
Release: alt1

Summary: A small utility to convert Unix lsof output to a graph showing FIFO and UNIX interprocess communication.
Group: System/Base
License: BSD-2
Url: https://github.com/zevv/lsofgraph
Packager: Andrey Bychkov <mrdrew@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar


%description
A small utility to convert Unix lsof output to a graph showing FIFO and 
UNIX interprocess communication.

%prep
%setup -q -n %name-%version

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
mv lsofgraph %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%doc README.md *.jpg LICENSE
%{_bindir}/*


%changelog
* Tue Apr 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
