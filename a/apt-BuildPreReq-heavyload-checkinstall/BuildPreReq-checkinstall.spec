# Guess whether the girar instance that is building us
# does not actually perform install checks.
#
# This guess can be overridden by: --with/--without install_check_in_girar
#
# * if it's a platform whose "official" girar instance is known (as of now)
# to skip the install checks
%ifarch %e2k
%def_without install_check_in_girar
%endif
# * or--to generalize--if the current build resembles that kind of girar instance
# by having another feature characteristic of the e2k girar,
# namely, --disable check
%if_disabled check
%def_without install_check_in_girar
%endif
%if_without check
%def_without install_check_in_girar
%endif
# * then we switch on the special behavior of our package
# to simulate an install check,
# * else (by default) we switch it off.
# (The %%def_with below won't have an effect if any of the %%def_without above
# have been evaluated.)
%def_with install_check_in_girar

# %%name should end with -checkinstall, because this is a special package,
# which shouldn't be visible by normal users.
Name: %(sed -Ee 's/(-checkinstall|)$/-checkinstall/' <<<'apt-BuildPreReq-heavyload-checkinstall')
Version: 1
Release: alt2

Summary: Empty package only useful during its build: it installs (and checks) another pkg
Group: Development/Other
License: CC0
URL: http://git.altlinux.org/people/imz/packages/BuildPreReq-checkinstall.git

BuildArch: noarch

%global other_pkg %(sed -Ee 's/BuildPreReq-//' <<<'apt-BuildPreReq-heavyload-checkinstall')

# The main effect of this package: just install another one during build.
# (Normally, the "checkinstall" component is not available for installation
# of the build dependencies. Luckily, the e2k Girar, which is the reason for
# the existence of this package, doesn't separate *-checkinstall packages.)
%if_without install_check_in_girar
BuildPreReq: %other_pkg
%define confirm_that_other_pkg_has_been_checked \
This build of this package has actually installed (and hence checked)\
%other_pkg_strictdep during the build.\
In other words, this phrase, which you are reading, is a confirmation\
that %other_pkg_strictdep\
has passed this kind of install check.
%endif

# Simulate an obligatory install check of every new release/build of %%other_pkg
# in this repository by adding a Requires on it and hence making an unmet dep appear
# if a new release/build of %%other_pkg is built in a task.
BuildRequires(pre): rpmquery-strictdep
%global other_pkg_strictdep %(rpmquery-strictdep %{other_pkg:shescape} || echo TO_SURVIVE_IN_HASHER_INITIALLY)
%if_without install_check_in_girar
Requires: %other_pkg_strictdep
%endif

%description
%summary:
%other_pkg

This package is only of interest for maintainers of the other package
(being tested).

So, whenever this package is rebuilt, the other package is installed
and its %%pre/%%post scripts are run, whereby the tests (if any) from
those scripts are executed. And this effect can be used to test
the other package:

* in a task in Girar by adding this package to the task (instead of
relying on the automatic install checks of Girar, in case the Girar
instance has the install checks turned off); the results can be seen
in srpm.log then;
* regularly in beehive (which rebuilds packages, but does no
install checks).
%{?confirm_that_other_pkg_has_been_checked}

This package also makes its best to guess whether the environment
where it is built looks like a Girar instance with install checks
turned off and, if so, simulates obligatory install checks by adding a
strict dependency on the release of the other package at the time of
build. (So that when a new build of the other package is done in a task
for this repository, there is an unmet dependency and the maintainer
is forced to add a rebuild of this package to the task.)

(Simulating an install check by means of a strict dep in a Girar
instance with install checks turned on would be redundant and cause an
unneeded excessive run of the tests in a single task and
an extra burden for the maintainer.)

Remark. The main idea of this package (to run tests during build)
won't normally work (in the usual instances of Girar or
beehive). The obstacle is that the other package whose scripts run
tests is usually a *-checkinstall package; but normally the
"checkinstall" component is not available for installation of the
build dependencies. However, by lucky coincidence, the Girar
instance that is of particular instance for us (i.e., the one that
has install checks turned off, namely, e2k) also doesn't currently
separate *-checkinstall packages into a repository component.

(There is another case where this deficiency is even for the better:
if one of the transitively required *-checkinstall packages
already runs the tests during its build, then running them once
again would be a redundant, excessive run of the tests, at least,
in beehive. Example: rpminstall-checkinstall req'd by rpm-checkinstall.
This isn't so much a concern in a Girar task, because
rpminstall-checkinstall isn't usually built in the same task as rpm.)

%files

%changelog
* Thu Dec 09 2021 Ivan Zakharyaschev <imz@altlinux.org> 1-alt2
- Added an URL.

* Wed Nov 10 2021 Ivan Zakharyaschev <imz@altlinux.org> 1-alt1
- Initial release for ALT Sisyphus (specially for
  testing packages on e2k instead of Girar's install checks).
