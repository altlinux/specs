Name: trace-summary
Version: 0.83
Release: alt1
Summary: A script generating break-downs of network traffic
Packager: Andriy Stepanov <stanv@altlinux.ru>
License: %bsd
Url: http://bro.org/sphinx/components/trace-summary/README.html
Source0: %name-%version.tar
BuildArch: noarch
Group: Networking/Other
BuildRequires: rpm-build-licenses
Requires: python-module-pysubnettree >= 0.23
Requires: ipsumdump

%description
trace-summary is a Python script that generates break-downs of network traffic,
including lists of the top hosts, protocols, ports, etc. Optionally, it can
generate output separately for incoming vs. outgoing traffic, per subnet, and
per time-interval.

%prep
%setup

%build
# nothing

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name

%files
%doc CHANGES COPYING README
%_bindir/%name

%changelog
* Mon Dec 29 2014 Andriy Stepanov <stanv@altlinux.ru> 0.83-alt1
- ALTLinux build

