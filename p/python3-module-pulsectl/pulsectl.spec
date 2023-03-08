%global pypi_name pulsectl

Name: python3-module-%{pypi_name}
Version: 22.3.2
Release: alt1
Summary: Python 3 high-level interface and ctypes-based bindings for PulseAudio
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/%{pypi_name}
Source: %{pypi_name}-%version.tar
# Source-url: https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools) python3(wheel)
#BuildRequires:  pulseaudio-libs

%description
Python 3 high-level interface and ctypes-based bindings
for PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).

%prep
%setup -n %{pypi_name}-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst CHANGES.rst
%python3_sitelibdir/%{pypi_name}/
%python3_sitelibdir/%{pypi_name}-%version.dist-info/

%changelog
* Thu Mar 09 2023 Anton Midyukov <antohami@altlinux.org> 22.3.2-alt1
- Initial build
