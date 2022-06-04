import { render, screen } from '@testing-library/react';
import header from './header';

test('renders learn react link', () => {
  render(<header />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
