%define        pkgname dynflow

Name:          ruby-%pkgname
Version:       1.2.3
Release:       alt1
Summary:       DYNamic workFLOW orchestration engine
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Dynflow/dynflow
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
%gem_replace_version concurrent-ruby-edge ~> 0.5

%description
%summary

%description -l ru_RU.UTF8
Движок для управления динамического рабочего потока.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Tue Jun 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.3-alt1
- Use Ruby Policy 2.0
- Bump to 1.2.3

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- Initial gemified build for Sisyphus
