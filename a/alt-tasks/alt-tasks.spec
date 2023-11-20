Name: alt-tasks
Version: 0.9.0
Release: alt2

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
* Fri Nov 17 2023 Alexey Appolonov <alexey@altlinux.org> 0.9.0-alt2
- Corrected copyright notices.

* Mon Nov 06 2023 Alexey Appolonov <alexey@altlinux.org> 0.9.0-alt1
- Ability to filter the results by src package names taken from a txt file;
- Ability to process all targets at once (with a single command).

* Sat Nov 04 2023 Alexey Appolonov <alexey@altlinux.org> 0.8.0-alt1
- Ability to filter resuls not only by a src package name, but also by its
  version and release;
- Branch names are displayed in the results.

* Wed Nov 01 2023 Alexey Appolonov <alexey@altlinux.org> 0.7.0-alt1
- The missing initial package versions are taken from the "plan/rm-src" files
  of the tasks.

* Fri Oct 27 2023 Alexey Appolonov <alexey@altlinux.org> 0.6.0-alt1
- A dump file is not used if the file "~/.alt-tasks/src_list" was modified after
  this dump file was created (rescan is performed).

* Sat Oct 14 2023 Alexey Appolonov <alexey@altlinux.org> 0.5.0-alt1
- Time saving on the processing the timelines of packages if a time of the
  previous processing is no latter than a requested "before" time (the dump
  file is used even if it's expired);
- The "after" param is checked to ensure that it doesn't exceed the current time
  (instead of getting an empty result, the program terminates with an error).

* Thu Oct 11 2023 Alexey Appolonov <alexey@altlinux.org> 0.4.0-alt1
- A previous version of a package is displayed for each subtask (use a new flag
  "--no_prev_ver" for the former behavior) as well as the "built from" part of
  a subtask commit designation ("gear" or "srpm").

* Mon Mar 01 2021 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt2
- Fixed build after new release of the "golang" package ("1.16-alt1").

* Fri Jul 03 2020 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- Ability to format the output according to a given format string;
- Ability to choose between verbose and not verbose output mode.

* Thu Jun 25 2020 Alexey Appolonov <alexey@altlinux.org> 0.2.1-alt1
- Couple of minor bug fixes.

* Fri Jun 19 2020 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Improved performance by the use of binary dumps.

* Tue May 12 2020 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
