Name: gnulib-modules-bootstrap
Version: 0.0.70.037f
Release: alt1

Summary: gnulib modules bootstrap
License: GPL-2.0-or-later or MIT
Group: Development/C
BuildArch: noarch
Url: https://github.com/gnulib-modules/bootstrap/
Source: %name-%version.tar
AutoReqProv: no

%description
This is a complete rewrite of the GNU Gnulib `bootstrap` script, for figuring
out what autotools need to be run, in what order, and with what arguments to
bootstrap a newly checked out working copy.  The author claims that this
version is much more robust, a lot more user friendly, slightly faster, and a
little more portable than the GNU version.  It's also quite a lot larger than
the GNU implementation.

%prep
%setup

%install
mkdir -p %buildroot%_datadir
cp -a . %buildroot%_datadir/%name

%files
%_datadir/%name/

%changelog
* Fri Mar 22 2019 Dmitry V. Levin <ldv@altlinux.org> 0.0.70.037f-alt1
- gnulib modules bootstrap snapshot 037f8376.
