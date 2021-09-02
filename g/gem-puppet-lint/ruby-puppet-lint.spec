%define        gemname puppet-lint

Name:          gem-puppet-lint
Epoch:         1
Version:       2.5.0
Release:       alt1
Summary:       Check that your Puppet manifests conform to the style guide
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rodjek/puppet-lint/
Vcs:           https://github.com/rodjek/puppet-lint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version puppet-lint:2.5.0
Obsoletes:     ruby-puppet-lint < %EVR
Provides:      ruby-puppet-lint = %EVR
Provides:      gem(puppet-lint) = 2.5.0


%description
The goal of this project is to implement as many of the recommended Puppet style
guidelines from the Puppet Labs style guide as practical. It is not meant to
validate syntax. Please use "puppet parser validate" for that.


%package       -n puppet-lint
Version:       2.5.0
Release:       alt1
Summary:       Check that your Puppet manifests conform to the style guide executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета puppet-lint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet-lint) = 2.5.0

%description   -n puppet-lint
Check that your Puppet manifests conform to the style guide executable(s).

The goal of this project is to implement as many of the recommended Puppet style
guidelines from the Puppet Labs style guide as practical. It is not meant to
validate syntax. Please use "puppet parser validate" for that.

%description   -n puppet-lint -l ru_RU.UTF-8
Исполнямка для самоцвета puppet-lint.


%package       -n gem-puppet-lint-doc
Version:       2.5.0
Release:       alt1
Summary:       Check that your Puppet manifests conform to the style guide documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet-lint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet-lint) = 2.5.0

%description   -n gem-puppet-lint-doc
Check that your Puppet manifests conform to the style guide documentation
files.

The goal of this project is to implement as many of the recommended Puppet style
guidelines from the Puppet Labs style guide as practical. It is not meant to
validate syntax. Please use "puppet parser validate" for that.

%description   -n gem-puppet-lint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet-lint.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n puppet-lint
%doc README.md
%_bindir/puppet-lint

%files         -n gem-puppet-lint-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1:2.5.0-alt1
- v 3.0.1 -> 2.5.0

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt0.1
^ 3.0.1 pre (really 2.3.6)
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 06 2017 Denis Medvedev <nbr@altlinux.org> 3.0.0-alt1
- bump to version 3.0.0

* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux
