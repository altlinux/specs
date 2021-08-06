Name:    moodle-qbehaviour_adaptive_adapted_for_coderunner
Version: 1.3.9
Release: alt1

Summary: The question behaviour required by the Moodle CodeRunner question type
License: GPL-3.0+
Group:   Other
Url:     https://github.com/trampgeek/moodle-qbehaviour_adaptive_adapted_for_coderunner

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-moodle

%description
This question behaviour was created solely for use with CodeRunner:
https://github.com/trampgeek/moodle-qtype_coderunner/. It provides the caching
of question test results needed to prevent re-testing a student's code every
time the result page is viewed.

%prep
%setup

%install
mkdir -p %buildroot%moodle_questiondir/behaviour/adaptive_adapted_for_coderunner
cp -a * %buildroot%moodle_questiondir/behaviour/adaptive_adapted_for_coderunner

%files
%doc *.md
%moodle_questiondir/behaviour/adaptive_adapted_for_coderunner

%changelog
* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- Initial build for Sisyphus.
