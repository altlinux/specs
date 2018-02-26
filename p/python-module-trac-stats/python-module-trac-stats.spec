Name: python-module-trac-stats
Version: 0.2
Release: alt1.1

Summary: The TracStatsPlugin adds a Stats tab to the trac project.

Group: Development/Python
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/TracStatsPlugin

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools

%description
The 'tracstats' plugin adds a "Stats" tab to the trac project. Underneath this
tab can be found statistics about subversion, wiki, and ticket system.

Some features include:

* Recent activity (last 30 days) showing top 10 developers, projects, and paths
  within the repository.

* Detailed statistics of source code development:

  * Total files by time
  * Commits by time, author, month, day of week, hour of day
  * Recent commits
  * Activity by time, author, project, filetype, change type
  * Most active paths, files
  * Commit cloud (built from checkin comments)

* Detailed statistics of Trac wiki pages:

  * Total pages by time
  * Edits by author
  * Latest wiki pages changed
  * Most active wiki pages
  * Largest wiki pages

* Detailed statistics of Trac tickets:

  * Open tickets by time
  * Tickets by author, component
  * Most active tickets
  * Oldest open tickets
  * Latest tickets reported, changed

%prep
%setup -q -n %name-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1
- initial build for ALT Linux Sisyphus
