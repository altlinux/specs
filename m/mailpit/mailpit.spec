%global import_path github.com/axllent/mailpit

%define _unpackaged_files_terminate_build 1

# Keep ui only for x86_64 to avoid node packages vendoring for each architecture
%ifarch x86_64
%def_with ui
%endif

Name: mailpit
Version: 1.29.1
Release: alt1

Summary: Mailpit - email & SMTP testing tool with API for developers
License: MIT
Group: Development/Tools
URL: https://mailpit.axllent.org/
VCS: https://github.com/axllent/mailpit

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: alt_vendor_golang.tar
Source2: alt_vendor_nodejs.tar

BuildRequires(pre): rpm-build-golang rpm-build-nodejs

%description
Mailpit is a small, fast, low memory, zero-dependency,
multi-platform email testing tool & API for developers.
It acts as an SMTP server, provides a modern web interface to view & test
captured emails, and includes an API for automated integration testing.

%prep
%setup -a1 -a2

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH

%if_with ui
npm run build
%endif

%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/%name
%doc README.md

%changelog
* Wed Mar 04 2026 Yaroslav Bahtin <alpacost@altlinux.org> 1.29.1-alt1
- Initial release

