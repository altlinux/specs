
Name:          taskjuggler
Version:       3.5.0
Release:       alt1
Summary:       Project management tool

Group:         Office
License:       GPLv2
URL:           http://www.taskjuggler.org
Source0:       http://www.taskjuggler.org/download/%{name}-%{version}.tar.bz2

Patch:         %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-term-ansicolor
BuildRequires: ruby-mail

%description
TaskJuggler is a modern and powerful project management tool. Its new
approach to project planning and tracking is far superior to the
commonly used Gantt chart editing tools. It has already been
successfully used in many projects and scales easily to projects with
hundreds of resources and thousands of tasks. It covers the complete
spectrum of project management tasks from the first idea to the
completion of the project. It assists you during project scoping,
resource assignment, cost and revenue planning, and risk and
communication management.

%prep
%setup -q
%patch -p1
%update_setup_rb

%build
%ruby_config --datadir=%_datadir/%name
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test ||:

%files
%doc README.rdoc TODO
%_bindir/*
%ruby_sitelibdir/*
%ruby_ri_sitedir/*
%_datadir/%name/*

%changelog
* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Wed Feb 06 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version 3.4.0

* Wed Feb 06 2013 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt2
- Fix build in Sisyphus
- Apply Fedora patches

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.1
- Fixed build

* Sat Mar 05 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- Return to Sisyphus

