Name: grep-warnings
Version: 1
Release: alt1

Summary: Extract and process warnings from build logs so that they can be compared

License: CC0
Group: Development/Other
Url: http://git.altlinux.org/gears/s/%name

BuildArch: noarch

Source0: grep-warnings
%global executable grep-warnings
Source1: %name-%version-tests.tar

%{?!_without_test:%{?!_disable_test:%{?!_without_check:%{?!_disable_check:BuildRequires: /usr/bin/diff /bin/bash /proc}}}}

%description
%executable extracts and processes warnings from build logs so that
two logs can be compared (by diff) to detect whether new warnings appeared.

Now it simply deletes line numbers from compiler warnings (because they might
differ after the source code changed.) It is suited to the format of warnings
produced by gcc or lcc.

Usage: %executable [--rpmb (p|c|i|STAGE)]

Usage example:

diff -d <(%executable --rpmb c <hsh.log.0 |sort) <(%executable --rpmb c <hsh.log.1 |sort)

%prep
%setup -T -b 1 -n %name-%version-tests
# In the testdata, the next lines after this warning have different numbers
# translated/untranslated messages, therefore we delete them
# to ignore these differences in our tests.
sed -re "/warning: header field 'Language' still has the initial default value/ d" \
    -i */hsh.log.*

%install
install -pm0755 -D %SOURCE0 -T %buildroot%_bindir/%executable

%check
GREP_WARNINGS=%buildroot%_bindir/%executable ./test.sh

%files
%_bindir/%executable

%changelog
* Sat Feb  8 2020 Ivan Zakharyaschev <imz@altlinux.org> 1-alt1
- initial build for ALT.


