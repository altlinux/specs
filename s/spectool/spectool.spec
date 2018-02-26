Summary: Display expanded Source/Patch macros from SPEC files
Name: spectool
Version: 1.0.9
Release: alt1
License: GPL
Group: Development/Other
# Upstream: Nils Philippsen <nphilipp$redhat,com>
URL: http://people.redhat.com/nphilipp/spectool/

Packager: Igor Vlasenko <viy@altlinux.org>

Source: http://people.redhat.com/nphilipp/spectool/spectool-%{version}.tar.bz2

BuildArch: noarch
BuildRequires: perl
Requires: perl, rpm-build

%description
spectool is a tool to display expanded Source/Patch macros from a SPEC file.

%prep
%setup

%build
%__subst s,fedora,altlinux, README spectool

%install
%{__install} -Dp -m0755 spectool %{buildroot}%{_bindir}/spectool

%files
%doc COPYING README
%{_bindir}/spectool

%changelog
* Wed Dec 05 2007 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1
- initial build (based on Dag Wieers's 1.0.7-fc7)

