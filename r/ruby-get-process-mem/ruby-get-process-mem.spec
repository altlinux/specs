# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname get-process-mem
%define        gemname get_process_mem

Name:          ruby-%pkgname
Version:       0.2.4
Release:       alt1
Summary:       Get memory usage of a process in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/schneems/get_process_mem
%vcs           https://github.com/schneems/get_process_mem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt1
- updated to (^) v0.2.4
- updated to (^) Ruby Policy 2.0

* Fri Oct 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus (without tests)
