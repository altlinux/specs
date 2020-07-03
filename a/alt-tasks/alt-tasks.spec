Name: alt-tasks
Version: 0.3.0
Release: alt1

Summary: Utility for observing ALT Linux tasks
License: GPLv3
Group: Other

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=alt-tasks.git
Source: %{name}-%{version}.tar

BuildRequires: golang

%description
%{name} recursively searches for and parses all "d-t-s-evr.list" files in
specified directories, then selects and prints out those tasks that satisfy
a given criteria.

%prep
%setup

%build
make tests
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp %{name}  %{buildroot}%{_bindir}
cp COPYING readme.txt %{buildroot}%{_defaultdocdir}/%{name}

%files
%{_bindir}/%{name}
%{_defaultdocdir}/%{name}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Fri Jul 03 2020 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- Ability to format the output according to a given format string;
- Ability to choose between verbose and not verbose output mode.

* Thu Jun 25 2020 Alexey Appolonov <alexey@altlinux.org> 0.2.1-alt1
- Couple of minor bug fixes.

* Fri Jun 19 2020 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Improved performance by the use of binary dumps.

* Tue May 12 2020 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
