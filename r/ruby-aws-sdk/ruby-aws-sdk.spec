%define  pkgname aws-sdk

Name: 	 ruby-%pkgname
Version: 2.10.85
Release: alt1

Summary: The official AWS SDK for Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://aws.amazon.com/ru/sdk-for-ruby/

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-ruby-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(kramdown)$/d

%description
The official AWS SDK for Ruby. Provides both resource oriented
interfaces and API clients for AWS services.

%package core
Summary: AWS SDK for Ruby - Core
Group:   Development/Ruby
Requires: ruby-jmespath

%description core
Provides API clients for AWS. This gem is part of the official AWS SDK
for Ruby.

%package resources
Summary: AWS SDK for Ruby - Resources
Group:   Development/Ruby
Requires: %name-core = %EVR

%description resources
Provides resource oriented interfaces and other higher-level
abstractions for many AWS services. This gem is part of the official AWS
SDK for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-ruby-%version

# Remove alterantive XML parser engines
rm -f aws-sdk-core/lib/aws-sdk-core/xml/parser/engines/{nokogiri,oga,ox,rexml}.rb

for dir in aws-sdk{,-core,-resources};do
	pushd $dir
	%update_setup_rb
	popd
done

%build
for dir in aws-sdk{,-core,-resources};do
	pushd $dir
	%ruby_config
	%ruby_build
	popd
done

%install
for dir in aws-sdk{,-core,-resources};do
	pushd $dir
	%ruby_install
	popd
done
%rdoc aws-sdk{,-core,-resources}/lib
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/aws-sdk.rb

%files core
%_bindir/aws.rb
%doc aws-sdk-core/*.json
%doc aws-sdk-core/*.crt
%ruby_sitelibdir/aws-sdk-core*
%ruby_sitelibdir/seahorse*

%files resources
%doc aws-sdk-resources/*.json
%ruby_sitelibdir/aws-sdk-resources*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Nov 17 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.85-alt1
- New version.

* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.84-alt1
- New version.

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.83-alt1
- New version.

* Fri Nov 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.82-alt1
- New version

* Thu Nov 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.81-alt1
- New version

* Wed Nov 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.80-alt1
- New version

* Tue Nov 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.79-alt1
- New version

* Sat Nov 04 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.78-alt1
- New version

* Fri Nov 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.77-alt1
- New version

* Thu Nov 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.76-alt1
- New version

* Fri Oct 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.74-alt1
- New version

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.71-alt1
- New version

* Tue Oct 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.70-alt1
- New version

* Sat Oct 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.69-alt1
- New version

* Fri Oct 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.68-alt1
- New version

* Thu Oct 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.67-alt1
- New version

* Wed Oct 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.66-alt1
- New version

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.65-alt1
- New version

* Fri Oct 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.64-alt1
- New version

* Wed Oct 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.62-alt1
- New version

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.61-alt1
- New version

* Fri Oct 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.59-alt1
- New version

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.58-alt1
- New version

* Wed Oct 04 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.57-alt1
- New version

* Tue Oct 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.56-alt1
- New version

* Sat Sep 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.55-alt1
- New version

* Thu Sep 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.54-alt1
- New version

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.53-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.52-alt1
- New version

* Thu Sep 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.50-alt1
- New version

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.49-alt1
- New version

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.48-alt1
- New version

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.47-alt1
- New version

* Fri Sep 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.46-alt1
- New version

* Thu Sep 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.45-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.44-alt1
- New version

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.40-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.38-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Sep 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.38-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.37-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.21-alt1
- Initial build for Sisyphus
