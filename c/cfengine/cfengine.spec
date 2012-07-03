%define unstable 0
%define workdir %_localstatedir/cfengine

Name: cfengine
Version: 3.1.1
Release: alt3.2
Group: System/Base
Summary: Atomation framework for system administration or IT Management.
License: %gpl3only
Url: http://www.cfengine.org
Packager: Andriy Stepanov <stanv@altlinux.ru>
Source0: %name-%version.tar
Source2: cf-monitord
Source3: cf-execd
Source4: cf-serverd
Source5: users_managment.cf
Patch1: cfengine-3-alt-config.patch
Patch2: cfengine-3-alt-build.patch

BuildRequires: flex libacl-devel libssl-devel glibc-devel-static libdb4-devel libgraphviz-devel libmysqlclient-devel libpcre-devel
BuildRequires: rpm-build-licenses

%description
Cfengine was designed to enable scalable configuration management,
for the whole system life-cycle, in any kind of environment.
Today it is the most advanced automation framework, supporting all
common platforms, and designed with security in mind, from the ground up.


%prep
%setup -q -n %name-%version
%patch1
%patch2 -p1

%build

%if %unstable
%define optflags_debug -g
%define _optlevel 0
%add_optflags %optflags_debug
%def_enable debug
%endif

export CFLAGS="%optflags"

%configure \
        %{subst_enable debug} \
        --with-workdir=%workdir \
        --with-graphviz
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
export LD_LIBRARY_PATH=$PWD/src/.libs
%make_build

%install
%make install DESTDIR=%buildroot

# Install service scripts
install -m 755 -d "%buildroot/%_initdir"
install -m 744 %{S:2} %{S:3} %{S:4} "%buildroot/%_initdir"

# Install own modules as examples
install -m 755 -d "%buildroot/%_defaultdocdir/%name"
install -m 644 %{S:5} "%buildroot/%_defaultdocdir/%name"

%preun
# Turn off and unregister services.
%preun_service cf-monitord
%preun_service cf-execd
%preun_service cf-serverd

%post
# Register services at first installation.
# Restart services at package updates.
%post_service cf-monitord
%post_service cf-execd
%post_service cf-serverd

##################################
# Follow fault tolerance design. #
##################################

##
# Placing CFengine inputs (default configuration) in the workdir.
# Configuration files updates for new CFengine version must be done manually.
#
if ! [ -d "%workdir/inputs" ]; then
      echo "Copy standard promises to CFengine workdir..."
      install -m 755 -d "%workdir/inputs"
      find "%_defaultdocdir/%name/inputs" -type f -exec install -m 600 '{}' "%workdir/inputs" ';'
      if [ -x "%_sbindir/cf-agent" -a -f "%workdir/inputs/failsafe.cf" ]; then
            echo "Bootstrap a cfengine configuration from failsafe file in the workdir..."
            "%_sbindir/cf-agent" --bootstrap
      fi
fi

%files
%doc AUTHORS ChangeLog README COPYING docs/ContributorStatement.pdf
%_libdir/lib*
%_sbindir/*
%_man8dir/*
%_defaultdocdir/%name
%_initdir/*

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt3.2
- Removed bad RPAYJ

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 3.1.1-alt3.1
- NMU: rebuilt with current graphviz

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.1-alt3
- fix build

* Fri Dec 03 2010 Andriy Stepanov <stanv@altlinux.ru> 3.1.1-alt2
- Rebuild with user managment module.

* Wed Dec 01 2010 Andriy Stepanov <stanv@altlinux.ru> 3.1.1-alt1
-  New version.
   Build static version instead shared.
   Add service files.

* Thu Nov 25 2010 Andriy Stepanov <stanv@altlinux.ru> 3.1.0-alt2
- Put binaries and inputs to CFengine workdir

* Sat Nov 13 2010 Andriy Stepanov <stanv@altlinux.ru> 3.1.0-alt1
- Build for ALTLinux
