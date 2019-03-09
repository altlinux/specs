%define        pkgname concourse

Name:          ruby-concourse
Version:       0.26.0
Release:       alt1
Summary:       Provide Rake tasks to ease management of Concourse pipelines. See https://concourse.ci/ to learn about Concourse.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/concourse-gem
# VCS:         https://github.com/flavorjones/concourse-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
The concourse gem provides rake tasks to help you manage Concourse CI pipelines,
jobs, and workers, to assist in running tasks with fly execute, and even run
a local ephemeral deployment of Concourse on your development machine.

If you're not familiar with Concourse CI, you can read up on it at
https://concourse-ci.org

%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.26.0-alt1
- Bump to 0.26.0.
- Use Ruby Policy 2.0.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- New version.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- Initial build for Sisyphus
