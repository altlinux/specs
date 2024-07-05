%define pyname ax
%define thislibdir %{python3_sitelibdir_noarch}/%{pyname}
%define thisdocdir %{_defaultdocdir}/%{name}

Name: python3-module-%{pyname}
Version: 0.19.0
Release: alt1

Summary: Generic function library initially developed for cve-manager
License: GPLv3
Group: Development/Python3

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=python3-module-ax.git
Source: %{pyname}.tar

BuildArch: noarch

BuildRequires: python3-devel
Requires: python3

%description
Python module with various helpfull features initially developed for
cve-manager project but potentially reusable elsewhere.

%prep
%setup -n %{pyname}

%build
make testing

%install
mkdir -p %{buildroot}%{thislibdir}
mkdir -p %{buildroot}%{thisdocdir}
# Executables
cp *.py %{buildroot}%{thislibdir}
# Documentation
cp COPYING %{buildroot}%{thisdocdir}

%files
%{thisdocdir}
%{thislibdir}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Thu Jul 04 2024 Alexey Appolonov <alexey@altlinux.org> 0.19.0-alt1
- New ability of the "Printer" class to display the time spent on each
  operation.

* Sat Apr 08 2023 Alexey Appolonov <alexey@altlinux.org> 0.18.0-alt1
- Ability to enable the "alerts only" and "plain" printing modes after
  initialization of a "Printer" object.

* Thu May 05 2022 Alexey Appolonov <alexey@altlinux.org> 0.17.1-alt1
- Improved algorithm of the "CompareLVersions" function;
- The name of a "Printer" class method that clears the stack of indentation
  levels is corrected.

* Wed Oct 27 2021 Alexey Appolonov <alexey@altlinux.org> 0.17.0-alt1
- Ability to control indentation levels while using the "Printer" class;
- Function "FormNestedDictFromCSV" is deprecated.

* Tue May 11 2021 Alexey Appolonov <alexey@altlinux.org> 0.16.1-alt1
- Fix of the "CompareSVerWithSRange" function.

* Sat Mar 06 2021 Alexey Appolonov <alexey@altlinux.org> 0.16.0-alt1
- New function "DateTimeNow" that returns a string with a current date and time
  in a customizable format;
- Modified function "PrepareDir" that returns an error message in addition to
  a formatted file path;
- Slightly enhanced "Printer" class.

* Tue Dec 15 2020 Alexey Appolonov <alexey@altlinux.org> 0.15.0-alt1
- New module 'vul' that can be used to extract vulnerability IDs from text.

* Wed Dec 09 2020 Alexey Appolonov <alexey@altlinux.org> 0.14.0-alt1
- New functions that help to work with versions that contain a date;
- Upgraded function 'SVerToLVer' that splits a given version not only into
  parts linked by delimiters in this version, but also into a year, month,
  and day of a date that may be found in this version.

* Thu Nov 26 2020 Alexey Appolonov <alexey@altlinux.org> 0.13.0-alt1
- Separate module 'ver' for working with software versions.

* Tue Nov 03 2020 Alexey Appolonov <alexey@altlinux.org> 0.12.0-alt1
- Ability to store many 'pages' of text in memory while using an object of
  the 'Printer' class.

* Thu Sep 17 2020 Alexey Appolonov <alexey@altlinux.org> 0.11.0-alt1
- Modified 'CompareLVersions' function that provides a more sophisticated way
  of comparing versions that have symbolic part at the right.

* Wed Sep 02 2020 Alexey Appolonov <alexey@altlinux.org> 0.10.0-alt1
- Modified 'CompareLVersions' function that gives an ability to check which
  of the two versions was recognized as symbolic (or neither, or both).

* Wed Jul 15 2020 Alexey Appolonov <alexey@altlinux.org> 0.9.0-alt1
- Enhanced 'Printer' class;
- Enhanced functions of version comparison;
- New function 'NearlyEqualShares' that helps to divide data (before processing
  that data in parallel, for example);
- The 'mode' module is deprecated.

* Mon Apr 20 2020 Alexey Appolonov <alexey@altlinux.org> 0.8.0-alt1
- Modified 'ReplaceNotAlfa' function of 'alt' module.

* Wed Mar 25 2020 Alexey Appolonov <alexey@altlinux.org> 0.7.0-alt1
- Enhanced 'SplitPackageName' function of 'alt' module.

* Tue Mar 03 2020 Alexey Appolonov <alexey@altlinux.org> 0.6.0-alt1
- Function that extracts name, version and release from a package name.

* Fri Jan 03 2020 Alexey Appolonov <alexey@altlinux.org> 0.5.0-alt1
- Functions for working with ranges of versions.

* Fri Dec 20 2019 Alexey Appolonov <alexey@altlinux.org> 0.4.0-alt1
- Optimized 'printer' module;
- Modified procedure of version comparisment.

* Fri Nov 29 2019 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- New submodule named 'alt' that helps to work with ALT Linux repos;
- Enhancement of 'Printer' class;
- Couple of new functions - one checks existence/access of a file and other
  prettifies string representation of a number.

* Wed Nov 20 2019 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Couple of new functions - one for searching files and one for removing
  duplicates from a given list.

* Sat Nov 16 2019 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release.
