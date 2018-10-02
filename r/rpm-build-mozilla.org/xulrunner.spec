Name: rpm-build-mozilla.org
Version: 41.0.2
Release: alt2
Summary: RPM helpers to build Mozilla.org packages
License: GPL
Group: Development/Other
BuildArch: noarch
Requires: raptor rpm-utils

Source: rpm-build.tar

%description -n rpm-build-mozilla.org
These helpers provide possibility to build Mozilla.org packages
by some Alt Linux Team Policy compatible way.

%prep
%setup -n rpm-build

%build

%install
install -Dm755 installrdf.sh %buildroot%_bindir/installrdf.sh
install -Dm755 applicationini.sh %buildroot%_bindir/applicationini.sh
sed -i \
        -e 's,@require_gre_name@,xulrunner,g' \
        -e 's,@rpmdatadir@,%_datadir/rpm-build-mozilla,g' \
        %buildroot%_bindir/*

install -D -m644 \
	mozilla-sh-functions \
	%buildroot/%_datadir/rpm-build-mozilla/mozilla-sh-functions

mkdir -p -- %buildroot/%_rpmmacrosdir
sed \
	-e 's,@xulr_name@,xulrunner,g' \
	-e 's,@xulr_version@,%version,g' \
	-e 's,@xulr_release@,%release,g' \
	rpm.macros.standalone > %buildroot%_rpmmacrosdir/xulrunner

%files
%_bindir/installrdf.sh
%_bindir/applicationini.sh
%_rpmmacrosdir/xulrunner
%_datadir/rpm-build-mozilla/mozilla-sh-functions

%changelog
* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 41.0.2-alt2
- Build rpm-build-mozilla.org separately from xulrunner.
