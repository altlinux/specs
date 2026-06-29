%global pypi_name ramalama
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 0.23.0
Release: alt1
Summary: RamaLama is a command line tool for working with AI LLM models
Group: Development/Python3

License: MIT
Url: https://github.com/containers/%pypi_name
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: python3-devel golang go-md2man
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-argcomplete

Requires: python3-module-%pypi_name = %EVR
Obsoletes: python3-module-%pypi_name < 0.10.1

%package -n python3-module-%pypi_name
Summary: %summary
Group: Development/Python3
Requires: bash-completion

%description
%summary

On first run RamaLama inspects your system for GPU support, falling back to CPU
support if no GPUs are present. It then uses container engines like Podman to
pull the appropriate OCI image with all of the software necessary to run an
AI Model for your systems setup. This eliminates the need for the user to
configure the system for AI themselves. After the initialization, RamaLama
will run the AI Models within a container based on the OCI image.

%description -n python3-module-%pypi_name
%summary

On first run RamaLama inspects your system for GPU support, falling back to CPU
support if no GPUs are present. It then uses container engines like Podman to
pull the appropriate OCI image with all of the software necessary to run an
AI Model for your systems setup. This eliminates the need for the user to
configure the system for AI themselves. After the initialization, RamaLama
will run the AI Models within a container based on the OCI image.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install
make DESTDIR=%buildroot PREFIX=%prefix install-docs install-shortnames
make DESTDIR=%buildroot PREFIX=%prefix install-completions

#%%check
#%%pyproject_run_pytest -v test/unit

%files
%doc docs/README.md
%_bindir/%pypi_name
%_datadir/bash-completion/completions/%pypi_name
%_datadir/fish/vendor_completions.d/ramalama.fish
%_datadir/zsh/site-functions/_ramalama
%dir %_datadir/%pypi_name
%_datadir/%pypi_name/shortnames.conf
%_datadir/%pypi_name/ramalama.conf
%_man1dir/ramalama*.1*
%_man5dir/ramalama*.5*
%_man7dir/ramalama*.7*

%files -n python3-module-%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Mon Jun 29 2026 L.A. Kostis <lakostis@altlinux.ru> 0.23.0-alt1
- 0.23.0.

* Sun May 17 2026 L.A. Kostis <lakostis@altlinux.ru> 0.21.0-alt1
- 0.21.0.

* Mon Apr 20 2026 L.A. Kostis <lakostis@altlinux.ru> 0.19.0-alt1
- 0.19.0.

* Sun Feb 08 2026 L.A. Kostis <lakostis@altlinux.ru> 0.17.1-alt1
- 0.17.1.

* Wed Jan 14 2026 L.A. Kostis <lakostis@altlinux.ru> 0.16.0-alt1
- 0.16.0.

* Sun Dec 14 2025 L.A. Kostis <lakostis@altlinux.ru> 0.15.0-alt1
- 0.15.0.

* Sun Nov 02 2025 L.A. Kostis <lakostis@altlinux.ru> 0.14.0-alt1
- 0.14.0.

* Tue Oct 28 2025 L.A. Kostis <lakostis@altlinux.ru> 0.13.0-alt1
- 0.13.0.

* Thu Oct 02 2025 L.A. Kostis <lakostis@altlinux.ru> 0.12.3-alt1
- 0.12.3.

* Thu Sep 18 2025 L.A. Kostis <lakostis@altlinux.ru> 0.12.2-alt1
- 0.12.2.

* Tue Aug 26 2025 L.A. Kostis <lakostis@altlinux.ru> 0.12.0-alt1
- 0.12.0.

* Wed Aug 06 2025 L.A. Kostis <lakostis@altlinux.ru> 0.11.3-alt1
- 0.11.3.

* Sun Jul 27 2025 L.A. Kostis <lakostis@altlinux.ru> 0.11.1-alt1
- 0.11.1.

* Mon Jul 14 2025 L.A. Kostis <lakostis@altlinux.ru> 0.11.0-alt1
- 0.11.0.
- split python3 module and ramalama itself.

* Tue Jul 01 2025 L.A. Kostis <lakostis@altlinux.ru> 0.10.0-alt1
- 0.10.0.

* Wed Jun 25 2025 L.A. Kostis <lakostis@altlinux.ru> 0.9.3-alt1
- 0.9.3.

* Tue Jun 17 2025 L.A. Kostis <lakostis@altlinux.ru> 0.9.2-alt1
- Initial build for ALTLinux.

