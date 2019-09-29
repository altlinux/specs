Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           abduco
Version:        0.6
Release:        alt1_8
Summary:        Session management in a clean and simple way

License:        ISC
URL:            http://www.brain-dump.org/projects/%{name}/
Source0:        %{url}/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
Source44: import.info

%description
%{name} provides session management i.e. it allows programs to be run
independently from its controlling terminal. That is programs can be
detached - run in the background - and then later reattached.
Together with dvtm it provides a simpler and cleaner alternative to tmux or
screen.

%prep
%setup -q
# Apply applicable build flags
echo '#!/bin/sh' > ./configure
chmod +x ./configure

%build
%configure
%make_build

%install
%makeinstall_std PREFIX=%{_prefix} STRIP=:

%files
%{!?_licensedir:%global license %doc}
%doc --no-dereference LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_8
- new version

