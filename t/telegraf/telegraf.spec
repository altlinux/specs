%global import_path github.com/influxdata/telegraf
%global commit a2d445326984b39ebb6f7c110384901448e101d9

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name:		telegraf
Version:	1.3.4
Release:	alt1
Summary:	The plugin-driven server agent for collecting and reporting metrics

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/telegraf

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	%name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

%description
Telegraf is an agent written in Go for collecting, processing, aggregating, and writing metrics.

Design goals are to have a minimal memory footprint with a plugin system so that developers
in the community can easily add support for collecting metrics from well known services
(like Hadoop, Postgres, or Redis) and third party APIs (like Mailchimp, AWS CloudWatch,
or Google Analytics).

%prep
%setup -q

%build
# Important!!!
# The %builddir/.gopath created by the hands. It contains the dependencies required for your project.
# This is necessary because the gdm cannot work with the vendor directory and always tries to update
# all dependencies from the external servers. So, we can't use Makefile to compile.
#
# $ export GOPATH="$PWD/.gopath"
# $ git rm -rf -- "$GOPATH"
# $ make
# $ find $GOPATH -type d -name .git |xargs rm -rf --
# $ git add "$GOPATH"

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot/%_datadir

%files
%_bindir/%name

%changelog
* Sun Jul 23 2017 Alexey Gladkov <legion@altlinux.ru> 1.3.4-alt1
- First build for ALTLinux.
