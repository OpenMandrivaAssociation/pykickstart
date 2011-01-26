Summary:  A python library for manipulating kickstart files
Name: pykickstart
Url: http://fedoraproject.org/wiki/pykickstart
Version: 1.77
Release: %mkrel 3
Source0: %{name}-%{version}.tar.gz
Patch10: pykickstart-1.77-post-packages.patch
License: GPLv2
Group: System/Libraries
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel, gettext, python-setuptools
Requires: python, python-urlgrabber

%description
The pykickstart package is a python library for manipulating kickstart
files.

%prep
%setup -q
%patch10 -p1

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog COPYING docs/programmers-guide
%doc docs/kickstart-docs.txt
%{python_sitelib}/*
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff

