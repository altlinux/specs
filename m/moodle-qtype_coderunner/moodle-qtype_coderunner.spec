Name:    moodle-qtype_coderunner
Version: 5.2.2
Release: alt1

Summary: A moodle quiz question type that runs student-submitted program code in a sandbox to check if it satisfies a given set of tests
License: GPL-3.0+
Group:   Education
Url:     http://coderunner.org.nz/
# VCS: https://github.com/trampgeek/moodle-qtype_coderunner 

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: alt-jobe-host-default.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-moodle
BuildRequires: rpm-build-python
BuildRequires: rpm-build-python3

Requires: moodle-base >= 3.8.0
Requires: moodle-qbehaviour_adaptive_adapted_for_coderunner
Requires: jobe
Requires: jobe-apache2

%filter_from_requires /^composer$/d
%add_python3_lib_path /var/www/webapps/moodle/question/type/coderunner/

%description
CodeRunner is a Moodle question type that allows teachers to run a program in
order to grade a student's answer. By far the most common use of CodeRunner is
in programming courses where students are asked to write program code to some
specification and that code is then graded by running it in a series of tests.
CodeRunner questions have also been used in other areas of computer science and
engineering to grade questions in which many different correct answers are
possible and a program must be used to assess correctness.

Regardless of the behaviour chosen for a quiz, CodeRunner questions always run
in an adaptive mode, in which students can click a Check button to see if their
code passes the tests defined in the question. If not, students can  resubmit,
typically for a small penalty. In the typical 'all-or-nothing' mode, all test
cases must pass if the submission is to be awarded any marks. The mark for a
set of questions in a quiz is then determined primarily by which questions the
student is able to solve successfully and then secondarily by how many
submissions the student makes on each question. However, it is also possible to
configure CodeRunner questions so that the mark is determined by how many of
the tests the code successfully passes.

%prep
%setup
%patch1 -p1

%install
mkdir -p %buildroot%moodle_questiondir/type/coderunner
cp -a * %buildroot%moodle_questiondir/type/coderunner

%files
%doc *.md
%moodle_questiondir/type/coderunner

%changelog
* Wed Oct 11 2023 Andrey Cherepanov <cas@altlinux.org> 5.2.2-alt1
- New version.

* Tue Aug 16 2022 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt1
- New version.

* Tue Aug 17 2021 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt2
- Use local jobe server.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- Initial build in Sisyphus.
