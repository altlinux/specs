%define _unpackaged_files_terminate_build 1
%define import_path github.com/MrJeffLarry/redmine-cli

Name: redmine-cli
Version: 0.1.7
Release: alt1

Summary: A software program that allows you to interact with the Redmine
License: MIT
Group: Networking/Other
Url: https://redmine-cli.hagerman.io
Vcs: https://github.com/MrJeffLarry/redmine-cli.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-%version-tags.tar
Source3: commit.sh

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Redmine-cli (Command Line Interface) is asoftware program that allows
you to interact with the Redmine project
management system using the command line.
With a Redmine CLI tool, you can perform
a wide range of tasks, such as creating and managing issues,
list projects, and more, all from the
comfort of your terminal or command prompt.

%prep
%setup -a1 -a2
%autopatch -p1

%build

cp %SOURCE3 .
chmod +x commit.sh
HASH=$(./commit.sh)

%make BIN_FOLDER=./bin/ \
  VERSION="%version" \
  GIT_COMMIT="$HASH" \
  build \
  #

%install
export BUILDDIR="$PWD"

%golang_install

%check
%make test

%files
%doc LICENSE
%_bindir/red-cli

%changelog
* Fri May 23 2025 Ivan Hanas <xeno@altlinux.org> 0.1.7-alt1
- New version.

* Sun May 18 2025 Ivan Khanas <xeno@altlinux.org> 0.1.6-alt1
- First Build for Alt Linux Sisyphus.
