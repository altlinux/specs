Name:    moodle-qbehaviour_adaptive_adapted_for_coderunner
Version: 1.4.3
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
* Wed Aug 07 2024 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- New version.

* Tue Aug 16 2022 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- New version.

* Sun Nov 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- New version.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- Initial build for Sisyphus.
