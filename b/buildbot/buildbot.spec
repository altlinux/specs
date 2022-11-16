Name: buildbot
Version: 3.6.1
Release: alt1
Summary: Python-based continuous integration testing framework

Group: Development/Python
License: GPLv2+
Url: https://buildbot.net

# https://github.com/buildbot/buildbot
Source: %name-%version.tar


###############################################################################
# Wheel sources
###############################################################################
Source1: buildbot_www-%version-py3-none-any.whl
Source2: buildbot_console_view-%version-py3-none-any.whl
Source3: buildbot_grid_view-%version-py3-none-any.whl
Source4: buildbot_waterfall_view-%version-py3-none-any.whl
Source5: buildbot_badges-%version-py3-none-any.whl
Source6: buildbot_wsgi_dashboards-%version-py3-none-any.whl


###############################################################################
# Completion sources
###############################################################################
Source21: _buildbot
Source22: _buildbot-worker


###############################################################################
# Systemd sources
###############################################################################
Source31: buildbot@.service
Source32: buildbot-worker@.service

Patch1: alt-disable-sending-usage-by-default.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Requires: python3-module-service-identity buildbot-www python3(msgpack)


###############################################################################
# Skip win requires
###############################################################################

%filter_from_requires /python3(pywintypes)/d
%filter_from_requires /python3(win32api)/d
%filter_from_requires /python3(win32con)/d
%filter_from_requires /python3(win32event)/d
%filter_from_requires /python3(win32file)/d
%filter_from_requires /python3(win32pipe)/d
%filter_from_requires /python3(win32process)/d
%filter_from_requires /python3(win32security)/d
%filter_from_requires /python3(win32service)/d
%filter_from_requires /python3(win32serviceutil)/d
%filter_from_requires /python3(winerror)/d


###############################################################################
# Main Package
###############################################################################

%description
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.


###############################################################################
# Package buildbot-worker
###############################################################################

%package worker
Group: Development/Python
Summary: Buildbot worker implementation
Requires: git-core python3(service_identity) python3(msgpack)

%description worker
%summary.


###############################################################################
# Package python3-module-buildbot-www
###############################################################################

%package -n python3-module-buildbot-www
Group: Development/Python
Summary: Buildboot web UI as python3 module

%description -n python3-module-buildbot-www
%summary.


###############################################################################
# Package buildbot-www
###############################################################################

# Need to create dummy package due to sisyphus_check limitations
%package www
Group: Development/Python
Summary: Buildbot web UI
Requires: python3-module-buildbot-www = %EVR

%description www
%summary.


###############################################################################
# Package python3-module-buildbot-www-extra-plugins
###############################################################################

%package -n python3-module-buildbot-www-extra-plugins
Group: Development/Python
Summary: Extra www plugins for buildboot as python3 module

%description -n python3-module-buildbot-www-extra-plugins
%summary.


###############################################################################
# Package buildbot-www-extra-plugins
###############################################################################

# Need to create dummy package due to sisyphus_check limitations
%package www-extra-plugins
Group: Development/Python
Summary: Extra www plugins for buildboot
Requires: python3-module-buildbot-www-extra-plugins = %EVR

%description www-extra-plugins
%summary.


###############################################################################
# Package buildbot-checkinstall
###############################################################################

%package checkinstall
Summary: Chekinstall for %name
Group: Other
BuildArch: noarch
Requires(pre): buildbot = %EVR buildbot-worker = %EVR buildbot-www = %EVR
Requires: /dev/pts python3-module-pbr python3-module-treq

%description checkinstall
%summary.


###############################################################################
# Build and Install
###############################################################################

%prep
%setup
%patch1 -p1

%build
for name in master worker; do
    pushd "$name"
    %python3_build_debug
    popd
done

%install
pushd master
%python3_install
install -Dm 0644 docs/buildbot.1 %buildroot/%_man1dir/buildbot.1
popd

pushd worker
%python3_install
install -Dm 0644 docs/buildbot-worker.1 %buildroot/%_man1dir/buildbot-worker.1
popd

python3 -mzipfile -e %SOURCE1 %buildroot/%python3_sitelibdir
python3 -mzipfile -e %SOURCE2 %buildroot/%python3_sitelibdir
python3 -mzipfile -e %SOURCE3 %buildroot/%python3_sitelibdir
python3 -mzipfile -e %SOURCE4 %buildroot/%python3_sitelibdir
python3 -mzipfile -e %SOURCE5 %buildroot/%python3_sitelibdir
python3 -mzipfile -e %SOURCE6 %buildroot/%python3_sitelibdir

install -Dm 0644 %SOURCE21 %buildroot/%_datadir/zsh/site-functions/_buildbot
install -Dm 0644 %SOURCE22 \
    %buildroot/%_datadir/zsh/site-functions/_buildbot-worker

mkdir -p %buildroot%_localstatedir/%{name}-worker
mkdir -p %buildroot%_localstatedir/%name

mkdir -p %buildroot%_unitdir
install -m 0644 %SOURCE31 %buildroot%_unitdir/
install -m 0644 %SOURCE32 %buildroot%_unitdir/

rm %buildroot%python3_sitelibdir/buildbot-*.egg-info/requires.txt


###############################################################################
# Pre
###############################################################################
%pre
groupadd -r -f _%name 2>/dev/null ||:
useradd -r -g _%name -c 'Buildbot master' \
        -d %_localstatedir/%name _%name 2>/dev/null ||:

%pre worker
groupadd -r -f _%{name}-worker 2>/dev/null ||:
useradd -r -g _%{name}-worker -c 'Buildbot worker' \
        -d %_localstatedir/%{name}-worker  _%{name}-worker 2>/dev/null ||:


###############################################################################
# Chekinstall
###############################################################################
%post checkinstall
# create and start master
buildbot create-master master
mv master/master.cfg.sample master/master.cfg
buildbot start master

# create and start worker
buildbot-worker create-worker worker localhost example-worker pass
buildbot-worker start worker


###############################################################################
# Files
###############################################################################

%files -n python3-module-buildbot-www
%python3_sitelibdir/buildbot_www
%python3_sitelibdir/buildbot_www-*.dist-info
%python3_sitelibdir/buildbot_console_view
%python3_sitelibdir/buildbot_console_view-*.dist-info
%python3_sitelibdir/buildbot_grid_view
%python3_sitelibdir/buildbot_grid_view-*.dist-info
%python3_sitelibdir/buildbot_waterfall_view
%python3_sitelibdir/buildbot_waterfall_view-*.dist-info

%files www

%files -n python3-module-buildbot-www-extra-plugins
%python3_sitelibdir/buildbot_badges
%python3_sitelibdir/buildbot_badges-*.dist-info
%python3_sitelibdir/buildbot_wsgi_dashboards
%python3_sitelibdir/buildbot_wsgi_dashboards-*.dist-info

%files www-extra-plugins

%files worker
%doc worker/docs
%_man1dir/buildbot-worker.1.*
%_bindir/buildbot-worker
%python3_sitelibdir/buildbot_worker
%python3_sitelibdir/buildbot_worker-*.egg-info
%dir %attr(0750,_%{name}-worker,_%{name}-worker) %_localstatedir/%{name}-worker
%_unitdir/%{name}-worker*
%_datadir/zsh/site-functions/_%{name}-worker

%files
%doc README.rst master/docs
%_man1dir/buildbot.1.*
%_bindir/buildbot
%python3_sitelibdir/buildbot
%python3_sitelibdir/buildbot-*.egg-info
%dir %attr(0750,_%name,_%name) %_localstatedir/%name
%_unitdir/%{name}*
%exclude %_unitdir/%{name}-worker*
%_datadir/zsh/site-functions/_%name

%files checkinstall

%changelog
* Tue Nov 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 3.6.1-alt1
- new version 3.6.1

* Sun Apr 10 2022 Mikhail Gordeev <obirvalger@altlinux.org> 3.5.0-alt1
- new version 3.5.0

* Thu Feb 10 2022 Mikhail Gordeev <obirvalger@altlinux.org> 3.4.1-alt1
- new version 3.4.1

* Mon Nov 01 2021 Mikhail Gordeev <obirvalger@altlinux.org> 3.4.0-alt1
- new version 3.4.0

* Mon Aug 09 2021 Mikhail Gordeev <obirvalger@altlinux.org> 3.3.0-alt1
- new version 3.3.0

* Wed Jun 23 2021 Mikhail Gordeev <obirvalger@altlinux.org> 3.2.0-alt1
- new version 3.2.0
- add zsh completion
- add service files

* Thu Apr 01 2021 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.2-alt1
- new version 3.0.2

* Wed Dec 23 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.9.3-alt2
- merge python3-module-buildbot-tests back into buildbot package, because
  buildbot.test.fake is used in buildbot dataspec

* Thu Dec 17 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.9.3-alt1
- new version 2.9.3
- enable tests via checkinstall

* Wed Oct 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.8.4-alt1
- new version 2.8.4

* Fri Mar 27 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.7.0-alt1
- new version 2.7.0

* Tue Jan 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.0-alt1
- update to 2.1.0

* Tue Jan 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.8.0-alt1
- update to 1.8.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.12-alt2.1
- Rebuild with Python-2.7

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.12-alt2
- add contrib to skip list

* Sat Feb 06 2010 Boris Savelev <boris@altlinux.org> 0.7.12-alt1
- new version

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.11p3-alt2.1
- Rebuilt with python 2.6

* Fri Nov 13 2009 Boris Savelev <boris@altlinux.org> 0.7.11p3-alt2
- move contrib to subpackage (closes: #22277)

* Mon Oct 12 2009 Boris Savelev <boris@altlinux.org> 0.7.11p3-alt1
- new version

* Thu Oct 01 2009 Boris Savelev <boris@altlinux.org> 0.7.10p1-alt1
- initial build for Sisyphus

* Thu Sep 10 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.7.10p1-2mdv2010.0
+ Revision: 436903
- rebuild

* Thu Mar 05 2009 Jérôme Soyer <saispo@mandriva.org> 0.7.10p1-1mdv2009.1
+ Revision: 348914
- New upstream release

* Sun Dec 28 2008 Funda Wang <fundawang@mandriva.org> 0.7.9-1mdv2009.1
+ Revision: 320366
- New version 0.7.9

* Mon Aug 11 2008 Jérôme Soyer <saispo@mandriva.org> 0.7.8-1mdv2009.0
+ Revision: 270612
- New release 0.7.8

* Thu Aug 07 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.7-2mdv2009.0
+ Revision: 266429
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Funda Wang <fundawang@mandriva.org> 0.7.7-1mdv2009.0
+ Revision: 195060
- New version 0.7.7

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.7.6-1mdv2008.1
+ Revision: 95946
- New release 0.7.6
- New release 0.7.6

* Thu Sep 27 2007 Anne Nicolas <anne.nicolas@mandriva.com> 0.7.5-3mdv2008.0
+ Revision: 93423
- bump release to reupload

* Wed Jun 06 2007 Jérôme Soyer <saispo@mandriva.org> 0.7.5-2mdv2008.0
+ Revision: 36098
- Fix %%mkrel number
- Bump release for rebuild
- Remove noarch
- Fix 64bits Build
- Fix RPM Group
- Import buildbot

